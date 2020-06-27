from django.shortcuts import render
from rest_framework import generics

from quiz.models import *
from .serializers import *


# Create your views here.
class QuizAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceAPIView(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSecretSerializer


class ChoiceSecretAPIView(generics.RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSecretSerializer


class ChoiceCheckAPIView(generics.RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceCheckSerializer
