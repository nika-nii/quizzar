from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    difficulty = models.IntegerField(default=0)

    def __str__(self):
        return "{title}, difficulty: {difficulty}".format(title=self.title, difficulty=self.difficulty)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "{title}".format(title=self.title)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)
    explanation = models.CharField(max_length=1000)

    def __str__(self):
        return "{correct}{text}".format(text=self.text, correct="✔" if self.correct else "✘")
