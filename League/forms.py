from django import forms
from .models import League

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['league_name', 'league_logo', 'number_of_teams', 'country', 'is_top5_league']
        widgets = {
            'league_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'League Name'}),
            'number_of_teams': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Teams'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'is_top5_league': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
