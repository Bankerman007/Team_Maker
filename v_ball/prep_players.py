import random
from v_ball.models import Player



def prep_players():
    lst= Player.objects.values('player_name', 'skill_level')
    players1 = []  
    

    for ele in lst:
        for key, value in ele.items():
            p = value
            players1.append(p)

    players = {players1[i]: players1[i + 1] for i in range(0, len(players1), 2)}
    other_players = list(map(lambda p: p[0], filter(_other_players, players.items())))   
    random.shuffle(other_players)
    top_players1 = list(map(lambda p: p[0], filter(_top_players, players.items())))

    return [top_players1, other_players]
    
def _top_players(player):
    return player[1] == 4
        
def _other_players(player):
    return player[1] != 4
        
prep_players()     
    
        
   




        

         
  

            

