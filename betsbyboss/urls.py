from django.conf.urls import url
from django.contrib import admin
from bets.views import about, free_bets, paid_bets, login, registration

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', about, name='about'),
    url(r'^bets$', free_bets, name='bets'),
    url(r'^vipbets$', paid_bets, name='vip-bets'),
    url(r'^login$', login, name='login'),
    url(r'^registration$', registration, name='registration'),
]
