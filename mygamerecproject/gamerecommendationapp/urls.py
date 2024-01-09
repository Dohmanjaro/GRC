# gamerecommendationapp/urls.py
from django.urls import path
from .views import game_details, home

urlpatterns = [
    path('game-details/<slug:game_slug>/', game_details, name='game_details'),
        path('', home, name='home'),
]
