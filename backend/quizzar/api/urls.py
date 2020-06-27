from django.urls import path

from .views import *

urlpatterns = [
    path('quiz', QuizAPIView.as_view()),
    path('quiz/<int:pk>/', QuizDetailAPIView.as_view()),
    path('question', QuestionAPIView.as_view()),
    path('question/<int:pk>/', QuestionDetailAPIView.as_view()),
    path('choice', ChoiceAPIView.as_view()),
    path('choice/<int:pk>/', ChoiceSecretAPIView.as_view()),
    path('choice/<int:pk>/check/', ChoiceCheckAPIView.as_view())
]