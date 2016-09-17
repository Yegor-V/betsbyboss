from django.conf.urls import url
from bets.views import free_bets, paid_bets, about, login, registration

urlpatterns = [
    url('^about$', about),
    url('^free_bets$', free_bets),
    url('^paid_bets$', paid_bets),
    url('^login$', login),
    url('^registration$', registration),

]
