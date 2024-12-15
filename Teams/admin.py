from django.contrib import admin
from .models import Teams
from django.utils.html import format_html

class TeamsAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'league', 'stadium', 'stadium_capacity', 'club_logo_preview')
    list_filter = ('league',)
    search_fields = ('team_name',)
    ordering = ('team_name',)
    list_per_page = 20

    # Customizing the team logo display in the admin panel list view
    def club_logo_preview(self, obj):
        if obj.club_logo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.club_logo.url)
        return "No Logo"
    club_logo_preview.short_description = 'Logo'

    # Fields displayed in the team form
    fieldsets = (
        (None, {
            'fields': ('team_name', 'club_logo', 'league', 'stadium', 'stadium_capacity')
        }),
    )

# Register the admin model
admin.site.register(Teams, TeamsAdmin)
