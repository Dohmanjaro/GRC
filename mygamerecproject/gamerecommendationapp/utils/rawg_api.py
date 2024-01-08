# gamerecommendationapp/utils/rawg_api.py

import requests
from decouple import config

RAWG_API_KEY = config('RAWG_API_KEY')
RAWG_API_BASE_URL = "https://api.rawg.io/api"

def get_game_details(game_slug):
    url = f"{RAWG_API_BASE_URL}/games/{game_slug}"

    params = {
        "key": RAWG_API_KEY,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        # Handle error, e.g., log the error or raise an exception
        return None
