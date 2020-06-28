from rest_framework import serializers

from quiz.models import Quiz, Question, Choice


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('pk', 'title', 'description', 'difficulty', 'questions')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk', 'title', 'description', 'choices')


class ChoiceSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('pk', 'text')


class ChoiceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('correct', 'explanation')
