from django.urls import path
from .views import QuizListCreateView

urlpatterns = [
    path('api/quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),    
]
