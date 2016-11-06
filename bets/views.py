from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Bet


class Bets(TemplateView):
    def get(self, request, *args, **kwargs):
        bets = Bet.objects.order_by('-date')[:5]
        return render(request, 'bets/free_bets.html', {'bets': bets})


class VipBets(TemplateView, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        bets = Bet.objects.order_by('-date')[:10]
        return render(request, 'bets/vip_bets.html', {'bets': bets})


def about(request):
    return render(request, 'bets/about.html', {})


def login(request):
    return render(request, 'bets/login.html', {})


def registration(request):
    return render(request, 'bets/registration.html', {})
