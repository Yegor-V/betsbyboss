from django.db import models
from tinymce.models import HTMLField


class Analytics(models.Model):
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    tournament_name = models.CharField(max_length=100)
    game_time = models.DateTimeField()
    is_live_bets = models.BooleanField()
    text = models.TextField()
    image = models.ImageField(upload_to='bets/static/bets/images')

    def __str__(self):
        return '{} vs {}'.format(self.team_1, self.team_2)

    @property
    def text_beginning(self):
        return ' '.join(self.text.split(' ')[:20]) + '...'

    @property
    def str_time(self):
        date_time = str(self.game_time)
        day = date_time.split('-')[2][0:2]
        month = date_time.split('-')[1]
        year = date_time.split('-')[0]
        time = date_time.split(' ')[1][0:5]
        return "{}/{}/{} {}".format(day, month, year, time)

    @property
    def crunch_image_path(self):
        image_name = str(self.image).split('/')[-1]
        return '/static/bets/images/' + image_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    editable_test = HTMLField()

    @property
    def text_beginning(self):
        return ' '.join(self.text.split(' ')[:100])
