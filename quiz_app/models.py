from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    """
    Model representing a quiz created by a user.
    Fields:
    - user: ForeignKey to the User model, indicating the creator of the quiz.
    - title: CharField for the title of the quiz.
    - description: TextField for a detailed description of the quiz.
    - created_at: DateTimeField to store the creation timestamp of the quiz.
    - updated_at: DateTimeField to store the last update timestamp of the quiz.
    - video_url: URLField to optionally store a related video URL for the quiz.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """String representation of the Quiz model, returning the title of the quiz."""
        return self.title

class Question(models.Model):
    """
    Model representing a question belonging to a quiz.
    Fields:
    - quiz: ForeignKey to the Quiz model, indicating which quiz the question belongs to.
    - question_title: CharField for the text of the question.
    - question_options: JSONField to store the options for the question as a list of strings.
    - answer: CharField to store the correct answer for the question.
    - created_at: DateTimeField to store the creation timestamp of the question.
    - updated_at: DateTimeField to store the last update timestamp of the question.
    """
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_title = models.CharField(max_length=500)
    question_options = models.JSONField(default=list) 
    answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Question model, returning the title of the question."""
        return self.question_title

