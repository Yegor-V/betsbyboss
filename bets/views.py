from django.shortcuts import render

from .models import Bet


def free_bets(request):
    bets = Bet.objects.order_by('-pub_date')[:5]
    return render(request, 'bets/free_bets.html', {'bets': bets})


def paid_bets(request):
    bets = Bet.objects.order_by('-pub_date')[:10]
    return render(request, 'bets/free_bets.html', {'bets': bets})


def about(request):
    return render(request, 'bets/about.html', {})


def login(request):
    return render(request, 'bets/login.html', {})


def registration(request):
    return render(request, 'bets/registration.html', {})
