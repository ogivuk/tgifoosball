from django.shortcuts import render, redirect
from django.http import HttpResponse
from tournament.models import Player, Tournament

def home_page(request):
    return render(request, 'home.html')

def view_tournament(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    return render(request,'tournament.html', {'tournament': tournament})

def new_tournament(request):
    tournament = Tournament.objects.create()
    Player.objects.create(name=request.POST['item_text'], tournament=tournament)
    return redirect(f'/tournament/{tournament.id}/')

def add_player(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    Player.objects.create(name=request.POST['item_text'], tournament=tournament)
    return redirect(f'/tournament/{tournament.id}/') 