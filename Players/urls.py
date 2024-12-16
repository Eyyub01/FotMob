from django.urls import path
from .views import Players_view

urlpatterns = [
    path('', Players_view, name='players'),
]