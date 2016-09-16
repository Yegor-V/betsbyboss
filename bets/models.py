from django.db import models
from django.utils import timezone


class Bet(models.Model):
    game_name = models.CharField(max_length=100)
    bet_amount = models.IntegerField()
    bet_for = models.CharField(max_length=20)
    pub_date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.game_name