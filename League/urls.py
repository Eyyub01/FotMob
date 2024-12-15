from django.urls import path
from .views import *

urlpatterns = [
    path('', leagues_view, name='League'),
    path('search/', leagues_search_view, name='search_leagues'),
    path('leagues/', leagues_filter_view, name='leagues'), 
]