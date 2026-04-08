from rest_framework import serializers
from quiz_app.models import Quiz, Question

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Question model, converting Question instances to and from JSON format.
    """
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options', 'answer', 'created_at', 'updated_at']

class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer for the Quiz model, converting Quiz instances to and from JSON format.
    Includes a nested representation of related questions using the QuestionSerializer.
    """

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'video_url', 'questions']
        read_only_fields = ['created_at', 'updated_at']

class CreateQuizSerializer(serializers.ModelSerializer):

    url = serializers.URLField(required=False, allow_blank=True)