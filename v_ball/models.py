from django.db import models

# Create your models here.

class Team(models.Model):
    team_name= models.CharField(max_length=30)
    total_points= models.IntegerField()
    
    
    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_name = models.CharField(max_length=30)
    skill_level = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="players")

    def __str__(self):
        return self.player_name






