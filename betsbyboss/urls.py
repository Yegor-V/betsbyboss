from django.conf.urls import url
from django.contrib import admin
from bets.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/?$', AboutView.as_view(), name='about'),
    url(r'^articles/?', ArticlesView.as_view(), name='articles'),
    url(r'^$', AnalyticsView.as_view(), name='analytics'),
]
