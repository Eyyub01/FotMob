from django.urls import path
from .views import teams_view

urlpatterns = [
    path('', teams_view, name='teams')
]