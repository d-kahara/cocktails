import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CocktailSerializer
from .models import Cocktail

class RandomCocktailView(APIView):
    """This endpoint returns a list of five random cocktails fetched from TheCocktailDB API
    """

    def get(self, request, *args, **kwargs):
        data = []
        for i in range(5):
            response = requests.get("http://www.thecocktaildb.com/api/json/v1/1/random.php")
            response_data = response.json().get('drinks')[0]
            serializer = CocktailSerializer(data=response_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data.append(serializer.data)
        return Response(data, status=status.HTTP_200_OK)

    
class CocktailDetailView(RetrieveUpdateDestroyAPIView):
    """This endpoint retrieves, updates or delets a single Cocktail's details given the id
    """

    serializer_class = CocktailSerializer
    lookup_url_kwarg = 'drink_id'
    queryset = Cocktail.objects.all()

class CustomCocktailCreateView(CreateAPIView):
    def post(self, request):
            serializer = CocktailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)