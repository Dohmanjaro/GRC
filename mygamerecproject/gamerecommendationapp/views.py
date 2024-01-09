# gamerecommendationapp/views.py
from django.shortcuts import render
from .utils.rawg_api import get_game_details, search_games

def game_details(request, game_slug="the-witcher-3-wild-hunt"):
    game_info = get_game_details(game_slug)

    if game_info:
        return render(request, "game_details.html", {"game_info": game_info})
    else:
        return render(request, "error.html")

def home(request):
    search_query = request.GET.get('search')  # Get the search query from the request

    if search_query:
        searched_games = search_games(search_query)
    else:
        searched_games = []

    return render(request, 'default_page.html', {'searched_games': searched_games})
