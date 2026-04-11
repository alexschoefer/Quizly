from rest_framework import generics, permissions, status, serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from quiz_app.models import Quiz, Question
from .serializers import QuizSerializer, CreateQuizSerializer
from .permissions import IsOwnerOfTheQuiz
from quiz_app.services.youtube_service import normalize_youtube_url, build_canonical_youtube_url, download_audio
from quiz_app.services.audio_transcription_service import transcribe_audio
from quiz_app.services.quiz_gemini_service import generate_quiz_from_transcript, validate_quiz_data
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
import os

@shared_task
def process_create_quiz_audio(quiz_id):
    """
    Asynchronous task to process the audio of a quiz's YouTube video, transcribe it, and update the quiz with the transcript and status.
    """
    try:
        quiz = Quiz.objects.get(id=quiz_id)
    except ObjectDoesNotExist:
        return

    audio_path = None

    try:
        audio_path = download_audio(quiz.video_url)
        transcript = transcribe_audio(audio_path)
        quiz_data = generate_quiz_from_transcript(transcript)
        validate_quiz_data(quiz_data)
        quiz.title = quiz_data["title"]
        quiz.description = quiz_data["description"]
        quiz.transcript = transcript
        quiz.status = "done"
        quiz.save()

        questions = [
            Question(
                quiz=quiz,
                question_title=q["question_title"],
                question_options=q["question_options"],
                answer=q["answer"],
            )
            for q in quiz_data["questions"]
        ]

        Question.objects.bulk_create(questions)

    except Exception as e:
        quiz.status = "failed"
        quiz.transcript = str(e)

    finally:
        quiz.save()

        if audio_path and os.path.exists(audio_path):
            os.remove(audio_path)

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
    
    def perform_create(self, serializer):
        """
        Override the default create behavior to handle YouTube video URL normalization and quiz creation.
        process_create_quiz_audio is called asynchronously to handle the audio processing after the quiz is created.
        """
        video_url = serializer.validated_data.get('url')

        if video_url:
            normalized_url = normalize_youtube_url(video_url)

            quiz = serializer.save(
                user=self.request.user,
                video_url=normalized_url,
                status="processing"
            )

            process_create_quiz_audio.delay(quiz.id)

        else:
            serializer.save(user=self.request.user)



