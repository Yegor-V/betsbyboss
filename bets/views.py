from django.views.generic import TemplateView, ListView
from bets.models import Article, Analytics


class AboutView(TemplateView):
    template_name = 'bets/about.html'


class AnalyticsView(ListView):
    template_name = 'bets/analytics.html'
    context_object_name = 'analytics'
    model = Analytics


class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'bets/articles.html'
