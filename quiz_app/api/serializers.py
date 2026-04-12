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

class CreateQuizSerializer(serializers.Serializer):
    """
    Serializer for creating a new Quiz instance, validating the input data for the title, description, and video URL fields.
    """
    url = serializers.URLField(required=False, allow_blank=True)

class UpdateQuizSerializer(serializers.ModelSerializer):
    """
    Serializer for updating Quiz instances, allowing partial updates of the title and description fields.
    """
    class Meta:
        model = Quiz
        fields = ['title', 'description']
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'title': {'required': False},
            'description': {'required': False},
        }




