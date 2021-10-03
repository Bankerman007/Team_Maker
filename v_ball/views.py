from django.shortcuts import redirect, render # render_to_response
from .forms import PlayerForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Team
from .models import Player

def base(request):
    return render(request, 'base.html',{})

def success(request):
    return render(request, 'success.html', {})

def home(request):
    players1 = Player.objects.all().filter(team = 1)
    team1 = { "name": "RED TEAM", "players": players1 }
    players2 = Player.objects.all().filter(team = 2)
    team2 = { "name": "BLUE TEAM", "players": players2 }
    players3 = Player.objects.all().filter(team = 3)
    team3 = { "name": "BLACK TEAM", "players": players3 }
    return render(request, 'home.html', { 'teams': [team1, team2, team3] })

def register(request):
    submitted = False
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = PlayerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register.html', {'form': form, 'submitted': submitted})