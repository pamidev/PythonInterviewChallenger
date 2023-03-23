from django.db import models


class QUESTIONS(models.Model):
    question = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    experience = models.ForeignKey('statistics.EXPERIENCE', on_delete=models.DO_NOTHING())
