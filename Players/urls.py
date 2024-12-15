from django.urls import path
from .views import Players_view

urlpatterns = [
    path('players/', Players_view, name='Players')
]