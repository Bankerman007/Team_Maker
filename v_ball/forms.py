from django import forms
from django.forms import ModelForm
from django.forms.widgets import Input
from .models import Player
from .models import Team

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name', 'skill_level', 'team',]
        player_name = forms.CharField()
        skill_level = forms.IntegerField()
        team = forms.CharField()

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name','total_points',]
        player_name = forms.CharField()
        team_name= forms.CharField(max_length=30)
        total_points= forms.IntegerField()

class Delete(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name',]
        #player_name = forms.CharField(max_length=30)
        player_name = forms.ModelMultipleChoiceField(queryset=Player.objects.all(),widget=forms.CheckboxSelectMultiple)

    