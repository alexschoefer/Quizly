from rest_framework import generics, permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from quiz_app.models import Quiz, Question
from .serializers import QuizSerializer, CreateQuizSerializer, UpdateQuizSerializer
from .permissions import IsOwnerOfTheQuiz
from quiz_app.services.youtube_service import normalize_youtube_url, build_canonical_youtube_url, download_audio
from quiz_app.services.audio_transcription_service import transcribe_audio
from quiz_app.services.quiz_gemini_service import generate_quiz_from_transcript, validate_quiz_data
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
import os
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied


class QuizListCreateView(generics.ListCreateAPIView):
    """
    API view to handle listing and creating quizzes. Only authenticated users can access this view.
    """
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Override the default serializer class based on the request method.
        """
        if self.request.method == 'POST':
            return CreateQuizSerializer
        return QuizSerializer
    
    def get_queryset(self):
        """
        Override the default queryset to return only quizzes created by the authenticated user.
        """
        return Quiz.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        """
        Override the default create method to handle YouTube video URL normalization and quiz creation. 
        The audio processing is done synchronously in this method for simplicity, but it can be moved to an asynchronous task if needed.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quiz = self._create_quiz(request, serializer)
        try:
            self._process_quiz(quiz)
            return self._success_response(quiz)

        except Exception as e:
            return self._error_response(quiz, e)

    # --- helper methods ---

    def _create_quiz(self, request, serializer):
        """
        Helper method to create a new quiz instance with the normalized YouTube video URL and initial status set to "processing".
        """
        return Quiz.objects.create(
            user=request.user,
            video_url=normalize_youtube_url(serializer.validated_data["url"]),
            status="processing"
        )

    def _process_quiz(self, quiz):
        """
        Helper method to handle the audio processing, transcription, quiz data generation, and quiz updating. This method can be moved to an asynchronous task if needed.
        """
        audio_path = download_audio(quiz.video_url)
        transcript = transcribe_audio(audio_path)

        quiz_data = generate_quiz_from_transcript(transcript)
        validate_quiz_data(quiz_data)

        quiz.title = quiz_data["title"]
        quiz.description = quiz_data["description"]
        quiz.transcript = transcript
        quiz.status = "done"
        quiz.save()

        Question.objects.bulk_create([
            Question(
                quiz=quiz,
                question_title=q["question_title"],
                question_options=q["question_options"],
                answer=q["answer"],
            )
            for q in quiz_data["questions"]
        ])

    def _success_response(self, quiz):
        """
        Helper method to return a successful response with the created quiz data.
        """
        return Response(QuizSerializer(quiz).data, status=201)

    def _error_response(self, quiz, error):
        """
        Helper method to handle errors during quiz processing, update the quiz status to "failed", and return an error response with the error message.
        """
        quiz.status = "failed"
        quiz.save()
        return Response({"error": str(error)}, status=500)

class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to handle retrieving, updating, and deleting a specific quiz. Only the owner of the quiz can access or modify it.
    """
    permission_classes = [IsAuthenticated, IsOwnerOfTheQuiz]

    def get_object(self):
        """
        Override the default get_object method to ensure that only the owner of the quiz can access or modify it.
        """
        quiz = generics.get_object_or_404(Quiz, id=self.kwargs['pk'])
        if quiz.user != self.request.user:
            if self.request.method == 'GET':
                raise PermissionDenied("You do not have permission to access this quiz.")
            else:
                raise PermissionDenied("You do not have permission to modify this quiz.")
        return quiz
    
    def get_serializer_class(self):
        """
        Override the default serializer class based on the request method.
        """
        if self.request.method == 'PATCH':
            return UpdateQuizSerializer
        return QuizSerializer
    
    def partial_update(self, request, *args, **kwargs):
        """
        Override the default partial_update method to handle partial updates of the quiz using the UpdateQuizSerializer.
        """
        quiz = self.get_object()
        serializer = self.get_serializer(quiz, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(QuizSerializer(quiz).data, status=status.HTTP_200_OK)