from django.urls import path
from .views import QuizListCreateView, QuizDetailView

urlpatterns = [
    path('api/quizzes/', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('api/quizzes/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),    
]
