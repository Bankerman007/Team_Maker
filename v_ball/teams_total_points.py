#from v_ball.make_teams import newteam1, newteam2, newteam3, newteam4, newteam5
from v_ball.models import Player 


def total_point_calc():

    red_team_points = 0
    blue_team_points = 0
    black_team_points= 0
    green_team_points= 0
    brown_team_points= 0

    players_red = Player.objects.all().filter(team = 1)
    players_blue = Player.objects.all().filter(team = 2)
    players_black = Player.objects.all().filter(team = 3)
    players_green = Player.objects.all().filter(team = 4)
    players_brown = Player.objects.all().filter(team = 5)
    
    
    for i in players_red:
        p = Player.objects.get(player_name = i)
        pp = p.skill_level
        red_team_points += pp    

    for i in players_blue:
        p = Player.objects.get(player_name = i)
        pp = p.skill_level
        blue_team_points += pp

    for i in players_black:
        p = Player.objects.get(player_name = i)
        pp = p.skill_level
        black_team_points += pp    
        
    for i in players_green:
        p = Player.objects.get(player_name = i)
        pp = p.skill_level
        green_team_points += pp

    for i in players_brown:
        p = Player.objects.get(player_name = i)
        pp = p.skill_level
        brown_team_points += pp

    return [red_team_points, blue_team_points, black_team_points, green_team_points, brown_team_points]

total_point_calc()

