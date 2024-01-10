from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import home, game_details

urlpatterns = [
    path('', home, name='home'),
    path('gamerecommendation/game-details/<str:game_slug>/', game_details, name='game_details'),

    # Use re_path to serve the React app
    re_path(r'^react-app/.*', TemplateView.as_view(template_name='frontend/my-react-app/build/index.html'), name='react_app'),
]