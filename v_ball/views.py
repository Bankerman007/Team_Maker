from django.shortcuts import redirect, render
from v_ball.teams_total_points import total_point_calc
from v_ball.prep_players import prep_players
from .forms import PlayerForm
from django.http import HttpResponseRedirect, request
from django.http import HttpResponse
from django import forms
from .models import Team
from .models import Player
from v_ball.make_teams import main



def base(request):
    return render(request, 'base.html',{})

def success(request):
    return render(request, 'success.html', {})

def home(request):
    [red_team_points, blue_team_points, black_team_points, green_team_points, brown_team_points] = total_point_calc()
    players1 = Player.objects.all().filter(team = 1)
    players2 = Player.objects.all().filter(team = 2)
    players3 = Player.objects.all().filter(team = 3)
    players4 = Player.objects.all().filter(team = 4)
    players5 = Player.objects.all().filter(team = 5)
    points_red = red_team_points
    points_blue = blue_team_points
    points_black = black_team_points
    points_green = green_team_points
    points_brown = brown_team_points

    return render(request, 'home.html', {'players1': players1, 'players2': players2, 'players3': players3,'players4': players4,'players5': players5, 'points_red':points_red, 'points_blue': points_blue, 'points_black':points_black, 'points_green': points_green, 'points_brown': points_brown})

def mix_teams(request):
    prep_players()
    main()
    return redirect('/')

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

def delete_players(request):
        players = Player.objects.all()
        return render(request,'delete_players.html',{'players':players})

def delete(request,id):   
        player = Player.objects.get(pk=id)
        player.delete()
        return redirect('/delete_players')

def edit_player(request,id):
    player = Player.objects.get(pk=id)
    form = PlayerForm(request.POST or None, instance=player)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/delete_players')
    return render(request, 'edit_player.html', {'player':player, 'form': form})

   
 