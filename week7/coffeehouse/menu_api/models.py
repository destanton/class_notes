from django.db import models


class Special(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.TextField()
