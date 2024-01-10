# gamerecommendationapp/views.py
from django.shortcuts import render
from .utils.rawg_api import get_game_details, search_games
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def game_details(request, game_slug):
    game_info = get_game_details(game_slug)

    if game_info:
        return render(request, "game_details.html", {"game_info": game_info})
    else:
        return render(request, "error.html")

# gamerecommendationapp/views.py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    search_query = request.GET.get('search')

    if search_query:
        searched_games = search_games(search_query, page_size=100)

        # Configure Paginator
        paginator = Paginator(searched_games, 10)  # Show 10 games per page

        # Get the current page number from the request
        page = request.GET.get('page')

        try:
            searched_games = paginator.page(page)

            print("Paginator Values:")
            print(f"Number of Pages: {paginator.num_pages}")
            print(f"Current Page Number: {page}")

        except PageNotAnInteger:
            # If page is not an integer, deliver the first page
            searched_games = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver the last page
            searched_games = paginator.page(paginator.num_pages)

        return render(request, 'default_page.html', {'searched_games': searched_games, 'search_query': search_query})
    else:
        return render(request, 'default_page.html', {'searched_games': []})