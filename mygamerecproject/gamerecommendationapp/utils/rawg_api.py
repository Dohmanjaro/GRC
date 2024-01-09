# gamerecommendationapp/utils/rawg_api.py

import requests
from datetime import date
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



def search_games(game_name):
    # Define parameters for the API request
    params = {
        'key': RAWG_API_KEY,
        'search': game_name,  # Specify the game name for the search
    }

    try:
        # Make the API request to the /autocomplete endpoint
        response = requests.get(f"{RAWG_API_BASE_URL}/games", params=params)
        response.raise_for_status()  # Raise an exception for unsuccessful responses

        # Debugging: Print the URL, status code, and the entire response content
        print("Request URL:", response.url)
        print("Status Code:", response.status_code)
        print("Response Content:", response.content)

        # Parse the JSON response
        data = response.json()

        # Debugging: Print the raw JSON response
        print("Raw JSON Response:", data)

        # Extract relevant information (modify as per the actual RAWG API response structure)
        searched_games = [
            {
                'name': game['name'],
                'slug': game['slug'],
                # Add more fields as needed
            }
            for game in data.get('results', [])
        ]

        return searched_games

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from RAWG API: {e}")
        return None