from django import forms
from django.forms import ModelForm
from django.forms.widgets import Input
from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['player_name', 'skill_level']
        player_name = forms.CharField()
        skill_level = forms.IntegerField()


    