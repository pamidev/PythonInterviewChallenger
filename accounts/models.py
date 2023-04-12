from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_creator = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    experience = models.ForeignKey('stats.Experience', on_delete=models.CASCADE)

class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
