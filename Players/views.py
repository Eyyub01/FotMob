from django.shortcuts import render
from .models import *

def Players_view(request):
    players_list = Player.objects.all
    context = {
        "players": players_list 
    }
    return render(request, 'players.html', context)