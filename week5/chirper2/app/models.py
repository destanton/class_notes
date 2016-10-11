from django.db import models


class Chirp(models.Model):
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
