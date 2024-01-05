from django.db import models
from django.contrib.auth.models import User


class FlashCard(models.Model):

    native_language = models.CharField(max_length=30)
    category = models.CharField(max_length=40)
    front_native = models.CharField(max_length=50)
    back_translation = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    known = models.IntegerField(default=0)

    def __str__(self):
        return self.front_native

