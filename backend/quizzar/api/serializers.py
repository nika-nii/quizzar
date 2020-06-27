from rest_framework import serializers

from quiz.models import Quiz, Question, Choice


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'description', 'difficulty')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('title', 'description')


class ChoiceSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('text',)


class ChoiceCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('correct', 'description')
