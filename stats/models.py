from django.db import models


class Experience(models.Model):
    lvl = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.lvl


# class AnswerHistory(models.Model):
#     user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
#     question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user
