from django.shortcuts import render
from rest_framework import generics

from quiz.models import Quiz
from .serializers import QuizSerializer


# Create your views here.
class QuizAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
