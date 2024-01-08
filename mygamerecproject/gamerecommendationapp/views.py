# gamerecommendationapp/views.py
from django.shortcuts import render
from .utils.rawg_api import get_game_details  # Import the utility function

def game_details(request, game_slug=None):
    if game_slug:
        # Use the RAWG API utility function to get game details
        game_info = get_game_details(game_slug)

        if game_info:
            # Render the template with game information
            return render(request, "game_details.html", {"game_info": game_info})
        else:
            # Handle error, e.g., display an error message
            return render(request, "error.html")
    else:
        # Handle the case where game_slug is not provided
        return render(request, "error.html")  # Add your error template or message
