from django.urls import path, include
from django.views.generic import TemplateView
from .views import home, game_details, search_view

urlpatterns = [
    path('', home, name='home'),
    path('gamerecommendation/game-details/<str:game_slug>/', game_details, name='game_details'),
    path('gamerecommendationapp/gamerecommendationapp/search', search_view, name='search_view'),  # Update this line

]