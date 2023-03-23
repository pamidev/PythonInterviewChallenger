from django.db import models


class Experience(models.Model):
    lvl = models.IntegerField(unique=True)


class AnswerHistory(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    question = models.ForeignKey('polls.Questions', on_delete=models.CASCADE)
