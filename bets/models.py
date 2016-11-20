from django.db import models


class Analytics(models.Model):
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    tournament_name = models.CharField(max_length=100)
    game_time = models.DateTimeField()
    is_live_bets = models.BooleanField()
    text = models.TextField()

    @property
    def text_beginning(self):
        return ' '.join(self.text.split(' ')[:10])


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    @property
    def text_beginning(self):
        return ' '.join(self.text.split(' ')[:100])
