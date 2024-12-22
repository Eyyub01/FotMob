from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_view, name='teams'),
    path('teams/', views.teams_search_view, name='teams_search')
]