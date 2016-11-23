from django.views.generic import TemplateView, ListView, DetailView
from bets.models import Article, Analytics


class AboutView(TemplateView):
    template_name = 'bets/about.html'


class AnalyticsView(ListView):
    template_name = 'bets/analytics.html'
    context_object_name = 'analytics'
    model = Analytics
    paginate_by = 2


class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'bets/articles.html'
    paginate_by = 2


class AnalyticsDetails(DetailView):
    model = Analytics
    template_name = 'bets/analytics_details.html'
    context_object_name = 'analytics'


class ArticleDetails(DetailView):
    model = Article
    template_name = 'bets/article_details.html'
    context_object_name = 'article'
