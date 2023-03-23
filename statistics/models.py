from django.db import models


class Experience(models.Model):
    lvl = models.IntegerField(unique=True)

class Answer_History(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    question = models.ForeignKey('Polls.Questions', on_delete=models.DO_NOTHING )