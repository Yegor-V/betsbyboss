from django.conf.urls import url, include
from django.contrib import admin
from bets.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^about/?$', AboutView.as_view(), name='about'),
    # url(r'^articles/?$', ArticlesView.as_view(), name='articles'),
    url(r'^articles/?$', CustomArticles.as_view(), name='articles'),
    url(r'^$', AnalyticsView.as_view(), name='analytics'),
    url(r'^analytics/(?P<pk>[0-9]+)$', AnalyticsDetails.as_view(), name='analytics-details'),
    url(r'^articles/(?P<pk>[0-9]+)$', ArticleDetails.as_view(), name='article-details'),
    url(r'^articles/the-boston-major/?$', BostonMajor.as_view(), name='boston-major'),
    url(r'^articles/the-boston-major-europe/?$', BostonMajorEurope.as_view(), name='boston-major-europe'),
    url(r'^articles/the-boston-major-usa/?$', BostonMajorUSA.as_view(), name='boston-major-usa'),

]
