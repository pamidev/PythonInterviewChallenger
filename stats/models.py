from django.db import models


class Experience(models.Model):
    lvl = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.lvl
