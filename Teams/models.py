from django.db import models
from League.models import League

class Teams(models.Model):
    team_name = models.CharField(max_length=64)
    club_logo = models.ImageField(null=True, blank=True)
    league = models.ForeignKey(League, models.CASCADE, null=True, blank=True)
    stadium = models.CharField(max_length=64, null=True, blank=True)
    stadium_capacity = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.team_name}'

    class Meta:
        verbose_name_plural = 'Teams'
