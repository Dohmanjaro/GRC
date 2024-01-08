# gamerecommendationapp/urls.py
from django.urls import path
from .views import game_details

urlpatterns = [
    # Add your other URL patterns if any
    path('game/<str:game_slug>/', game_details, name='game_details'),
]
