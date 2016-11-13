from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
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


class Articles(ListView):
    template_name = 'bets/articles.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 1

    def get_queryset(self):
        return Article.objects.all().order_by('-date')


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
