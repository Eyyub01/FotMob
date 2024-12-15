from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'position', 'team', 'height', 'preferred_foot')
    search_fields = ('full_name', 'team__team_name')  # Searching by player's full name or team name

admin.site.register(Player, PlayerAdmin)
