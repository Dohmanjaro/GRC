# api/urls.py
from django.urls import path
from .views import YourModelList

urlpatterns = [
    path('your-model/', YourModelList.as_view(), name='your-model-list'),
    # Add more patterns for other views as needed
]
