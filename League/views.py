from django.shortcuts import render, redirect
from .models import League

from django.db.models import Q
from django.db.models import Q
from django_countries import countries
from .forms import LeagueForm
from django.contrib import messages


def leagues_view(request):
    league_listing = League.objects.all()
    context = {
        "leagues": league_listing
    }
    return render(request, 'home.html', context)


def leagues_search_view(request):
    query = request.GET.get('q', '')  # Retrieve the search query from the URL (default is empty string)
    
    leagues = League.objects.all()  # Start with all leagues
    
    if query:
        # Try matching the country code by name
        country_codes = [code for code, name in countries if query.lower() in name.lower()]
        
        # Filter leagues by name or by country code
        leagues = leagues.filter(
            Q(league_name__icontains=query) | Q(country__in=country_codes)
        )
    
    return render(request, 'home.html', {'leagues': leagues, 'query': query})



def leagues_filter_view(request):
    filter_type = request.GET.get('filter', 'all')  # Get filter type from query params
    if filter_type == 'top5':
        leagues = League.objects.filter(is_top5_league=True)  # Only Top-5 leagues
    else:
        leagues = League.objects.all()  # Show all leagues by default

    return render(request, 'home.html', {'leagues': leagues, 'filter_type': filter_type})


def add_league(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "League added successfully!")
            return redirect('leagues')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LeagueForm()
    return render(request, 'add_league.html', {'form': form})