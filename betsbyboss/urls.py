from django.conf.urls import url
from django.contrib import admin

from bets.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^about$', about, name='about'),
    url(r'^$', Bets.as_view(), name='bets'),
    url(r'^vipbets$', VipBets.as_view(), name='vip-bets'),
    url(r'^login/?$', user_login, name='login'),
    url(r'^registration$', registration, name='registration'),
    url(r'^articles', Articles.as_view(), name='articles'),
]
