from django.contrib import admin
from .models import *

class LeagueAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('league_name', 'country', 'number_of_teams', 'is_top5_league')
    
    # Add search functionality
    search_fields = ('league_name', 'country')
    
    # Add filter options
    list_filter = ('is_top5_league', 'country', 'number_of_teams')
    
    # Add ordering (optional)
    ordering = ('league_name',)
    
    # Enable clickable fields
    list_display_links = ('league_name',)

# Register the model with the customized admin class
admin.site.register(League, LeagueAdmin)

admin.site.site_header = "FotMob Administration"
admin.site.site_title = "FotMob Admin Panel"
admin.site.index_title = "Welcome to FotMob Admin"
