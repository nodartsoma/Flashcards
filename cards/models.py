from django.db import models
from django.contrib.auth.models import User


class Flashcard(models.Model):
    LANGUAGES = (("English", "English"),
                 ("French", "French"),
                 ("Spanish", "Spanish"),
                 ("German", "German"),
                 ("Russian", "Russian"),
                 ("Italian", "Italian"))

    native_language = models.CharField(max_length=30, choices=LANGUAGES)
    category = models.CharField(max_length=40)
    front_native = models.CharField(max_length=50)
    back_translation = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.front_native

