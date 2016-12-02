from django.views.generic import TemplateView, ListView, DetailView
from bets.models import Article, Analytics


class AboutView(TemplateView):
    template_name = 'bets/about.html'


class AnalyticsView(ListView):
    template_name = 'bets/analytics.html'
    context_object_name = 'analytics'
    model = Analytics
    paginate_by = 10
    queryset = Analytics.objects.all().order_by('-game_time')


class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'bets/articles.html'
    paginate_by = 5


class AnalyticsDetails(DetailView):
    model = Analytics
    template_name = 'bets/analytics_details.html'
    context_object_name = 'analytics'


class ArticleDetails(DetailView):
    model = Article
    template_name = 'bets/article_details.html'
    context_object_name = 'article'


class BostonMajor(TemplateView):
    template_name = 'bets/boston_major.html'


class CustomArticles(TemplateView):
    template_name = 'bets/custom_articles.html'


class BostonMajorEurope(TemplateView):
    template_name = 'bets/boston_major_europe.html'


class BostonMajorUSA(TemplateView):
    template_name = 'bets/boston_major_usa.html'

