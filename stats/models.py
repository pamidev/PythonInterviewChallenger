from django.db import models


class Experience(models.Model):
    lvl = models.CharField(max_length=10, unique=True)


class AnswerHistory(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
