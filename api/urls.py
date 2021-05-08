from django.urls import path

from .views import CocktailDetailView,CustomCocktailCreateView, RandomCocktailView

app_name = "api"


urlpatterns = [
    path("cocktails/random/", RandomCocktailView.as_view(), name='random-cocktails'),
    path("cocktails/<int:drink_id>/", CocktailDetailView.as_view(), name='cocktails'),
    path("cocktails/", CustomCocktailCreateView.as_view(), name='create-custom-cocktail')
    ]