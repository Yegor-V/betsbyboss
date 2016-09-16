from django.conf.urls import url
from bets.views import bets_list

urlpatterns = [
    url('^$', bets_list)
]
