from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator
from datetime import date
from Teams.models import Teams  # Ensure this import matches your actual Teams model import

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('LB', 'Left Back'),
        ('CB', 'Center Back'),
        ('RB', 'Right Back'),
        ('LWB', 'Left Wing Back'),
        ('RWB', 'Right Wing Back'),
        ('DM', 'Defensive Midfielder'),
        ('CM', 'Center Midfielder'),
        ('AM', 'Attacking Midfielder'),
        ('LM', 'Left Midfielder'),
        ('RM', 'Right Midfielder'),
        ('LW', 'Left Winger'),
        ('RW', 'Right Winger'),
        ('CF', 'Center Forward'),
        ('SS', 'Second Striker'),
        ('ST', 'Striker')
    ]
    
    PREFERRED_FOOT_CHOICES = [
        ('R', 'Right'),
        ('L', 'Left'),
        ('B', 'Both')
    ]
    
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=64)
    country = CountryField()
    date_of_birth = models.DateField(null=True, blank=True, help_text='Please write in order YEAR-MONTH-DAY')
    player_photo = models.ImageField(null=True, blank=True)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    height = models.PositiveIntegerField(validators=[MinValueValidator(150)])
    preferred_foot = models.CharField(max_length=1, choices=PREFERRED_FOOT_CHOICES, null=True, blank=True)

    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age

    def __str__(self):
        return f"{self.full_name} - {self.age()}"

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
