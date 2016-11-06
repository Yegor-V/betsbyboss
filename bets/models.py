from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Bet(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Owner(User):
    is_boss = models.BooleanField()


class BBBUser(User):
    key_to_private = models.CharField(max_length=100, default=None)
    key_expires = models.DateTimeField()

    @property
    def has_key(self):
        if self.key_to_private:
            if timezone.now() >= self.key_expires:
                return True
        return False
