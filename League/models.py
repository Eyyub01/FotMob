from django.db import models
from django_countries.fields import CountryField

class League(models.Model):
    league_name = models.CharField(max_length=64)
    league_logo = models.ImageField(null=True, blank=True, upload_to='league_logos/')
    number_of_teams = models.PositiveSmallIntegerField()
    country = CountryField()
    is_top5_league = models.BooleanField('Top-5 League', default=False)

    def __str__(self):
        return f'{self.league_name}'
