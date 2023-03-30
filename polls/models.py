from django.db import models
from django.utils import timezone


class Question(models.Model):
    question = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    is_verified = models.BooleanField(default=False)
    experience = models.ForeignKey('stats.Experience', on_delete=models.CASCADE)

    def __str__(self):
        return self.question
