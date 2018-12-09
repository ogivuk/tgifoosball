from django.shortcuts import render, redirect
from django.http import HttpResponse
from tournament.models import Player

def home_page(request):
    if request.method == "POST":
        Player.objects.create(name=request.POST['item_text'])
        return redirect('/')

    players = Player.objects.all()
    return render(request, 'home.html', {'players': players})
