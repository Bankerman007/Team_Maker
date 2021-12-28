
from v_ball.prep_players import prep_players
from v_ball.models import Player
from v_ball.models import Team

def main():
    [top_players1, other_players] = prep_players()
    team1 = top_players1[0]
    team2 = top_players1[1]
    team3 = top_players1[2]
    team4 = top_players1[3]
    team5 = top_players1[4]
    newteam1 = [team1,]
    newteam2 = [team2,]
    newteam3 = [team3,]
    newteam4 = [team4,]
    newteam5 = [team5,]

    for p in other_players:
        if len(newteam1) < 4:
            newteam1.append(p)            
        elif len(newteam2) < 4:
            newteam2.append(p)
        elif len(newteam3) < 4:
            newteam3.append(p)
        elif len(newteam4) < 4:
            newteam4.append(p)           
        else:
            newteam5.append(p)
    

    red_team = Team.objects.get(team_name = 'Red')
    blue_team = Team.objects.get(team_name = 'Blue')
    black_team = Team.objects.get(team_name = 'Black')
    green_team = Team.objects.get(team_name = 'Green')
    brown_team = Team.objects.get(team_name = 'Brown')

    for i in newteam1:
        ct = Player.objects.get(player_name = i)
        ct.team = red_team
        ct.save()

    for i in newteam2:
        ct = Player.objects.get(player_name=i)
        ct.team = blue_team
        ct.save()

    for i in newteam3:
        ct = Player.objects.get(player_name=i)
        ct.team = black_team
        ct.save()

    for i in newteam4:
        ct = Player.objects.get(player_name=i)
        ct.team = green_team
        ct.save()

    for i in newteam5:
        ct = Player.objects.get(player_name=i)
        ct.team = brown_team
        ct.save()


if __name__ == "__main__":
    main()


