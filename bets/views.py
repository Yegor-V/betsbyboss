from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView

from .models import *


class Bets(TemplateView):
    def get(self, request, *args, **kwargs):
        bets = Bet.objects.order_by('-date')[:5]
        return render(request, 'bets/free_bets.html', {'bets': bets})


class VipBets(LoginRequiredMixin, TemplateView):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        bets = Bet.objects.order_by('-date')[:10]
        return render(request, 'bets/vip_bets.html', {'bets': bets})


def about(request):
    return render(request, 'bets/about.html', {})


class Articles(View):
    def get(self, request, *args, **kwargs):

        all_articles = Article.objects.all().order_by('-date')
        articles = []
        for article in all_articles:
            text_beginning = ' '.join(article.text.split(' ')[:100])
            articles.append({'title': article.title, 'date': article.date, 'text': text_beginning})

        return render(request, 'bets/articles.html', {'articles': articles})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, 'bets/login.html', {'error': 'user does not exist or wrong password'})
    else:
        return render(request, 'bets/login.html')


def registration(request):
    return render(request, 'bets/registration.html', {})
