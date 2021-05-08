from django.urls import path

from .views import (CocktailDetailView, CustomCocktailCreateView,
                    FetchRecentCocktails, RandomCocktailView)

app_name = "api"


urlpatterns = [
    path("cocktails/random/", RandomCocktailView.as_view(), name='random-cocktails'),
    path("cocktails/recent/", FetchRecentCocktails.as_view(), name='recent-cocktails'),
    path("cocktails/<int:drink_id>/", CocktailDetailView.as_view(), name='cocktails-detail'),
    path("cocktails/", CustomCocktailCreateView.as_view(), name='create-custom-cocktail')
    ]
