from django.conf.urls import url, include
from django.contrib import admin
from bets.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bets/', include('bets.urls')),
    url(r'^$', index),
]
