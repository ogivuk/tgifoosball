from django.shortcuts import render, redirect
from django.http import HttpResponse
from tournament.models import Player

def home_page(request):
    if request.method == "POST":
        Player.objects.create(name=request.POST['item_text'])
        return redirect('/tournament/the-only-tournament-in-the-world/')
    return render(request, 'home.html')

def view_tournament(request):
    players = Player.objects.all()
    return render(request,'tournament.html', {'players': players})
