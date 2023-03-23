from django.db import models


class USER(models.MODEL):
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_creator = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    experience = models.ForeignKey('STATISTICS.EXPERIENCE', on_delete=models.DO_NOTHING)