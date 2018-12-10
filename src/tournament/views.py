from django.shortcuts import render, redirect
from django.http import HttpResponse
from tournament.models import Player, Tournament

def home_page(request):
    return render(request, 'home.html')

def view_tournament(request):
    players = Player.objects.all()
    return render(request,'tournament.html', {'players': players})

def new_tournament(request):
    tournament = Tournament.objects.create()
    Player.objects.create(name=request.POST['item_text'], tournament=tournament)
    return redirect('/tournament/the-only-tournament-in-the-world/')