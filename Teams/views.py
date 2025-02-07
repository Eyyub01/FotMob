from django.shortcuts import render
from .models import Teams
from League.models import League


def teams_view(request):
    teams_list = Teams.objects.all
    context = {
        "teams": teams_list 
    }
    return render(request, 'teams.html', context)


def teams_view(request):
    # Get all leagues for filter options
    leagues = League.objects.all()

    # Filter teams by league if 'league' parameter is passed in the URL
    selected_league = request.GET.get('league')
    if selected_league:
        teams = Teams.objects.filter(league__id=selected_league)
    else:
        teams = Teams.objects.all()

    return render(request, 'teams.html', {'teams': teams, 'leagues': leagues, 'selected_league': selected_league})


def teams_search_view(request):
    query = request.GET.get('q')  # Get the search term from the query string
    teams = Teams.objects.all()

    if query:
        teams = teams.filter(team_name__icontains=query)  # Case-insensitive search for team names

    context = {
        'teams': teams,
        'query': query,
    }
    return render(request, 'teams.html', context)

