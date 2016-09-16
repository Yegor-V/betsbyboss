from django.shortcuts import render

from .models import Bet


def bets_list(request):
    bets = Bet.objects.order_by('-pub_date')[:10]
    return render(request, 'bets/index.html', {'bets': bets})
