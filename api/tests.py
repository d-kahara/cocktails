import pytest
import json

from rest_framework import status
from django.urls import reverse
from api.models import Cocktail


class TestCocktailCRUD(object):
    @pytest.mark.django_db
    def test_get_cocktails_list_succeeds(self, client):
        url = reverse('api:recent-cocktails')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_cocktail_model_save_succeeds(self, new_cocktail):
        new_cocktail.save()
        assert Cocktail.objects.count() == 1


    @pytest.mark.django_db
    def test_create_custom_cocktail_succeeds(self, client):
        """Test creating a custom cocktail """
        data = {
            "strDrink": "ratish",
            "strDrinkAlternate": "spirit of Africa",
            "strTags": "spirit",
            "strVideo": "",
            "strIBA": "",
            "strAlcoholic": "Akoho",
            "strGlass": "jug daniels",
        }
        url = reverse('api:create-custom-cocktail')
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get('strDrink') == data.get('strDrink')
        assert response.data.get('strAlcoholic') == data.get('strAlcoholic')
        assert response.data.get('strGlass') == data.get('strGlass')

    @pytest.mark.django_db
    def test_read_cocktail_succeeds(self, client,  new_cocktail):
        """Test getting an existing cocktail """
       
        new_cocktail.save()
        latest_cocktail = Cocktail.objects.latest('id')
        url = reverse('api:cocktails-detail', args=[str(latest_cocktail.id)])
        response = client.get(url, content_type='application/json')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_update_cocktail_succeeds(self, client, new_cocktail):
        """Test editing of an existing cocktail """
        new_cocktail.save()
        update_data = {
            "strDrink": "Hennessy",
        }
        latest_cocktail = Cocktail.objects.latest('id')
        assert latest_cocktail.strDrink == "Konyagi"
        url = reverse('api:cocktails-detail', args=[str(latest_cocktail.id)])
        response = client.patch(url, data=json.dumps(update_data),
                            content_type='application/json')
        latest_cocktail = Cocktail.objects.latest('id')
        assert response.status_code == status.HTTP_200_OK
        assert latest_cocktail.strDrink == "Hennessy"

    @pytest.mark.django_db
    def test_delete_cocktail_succeeds(self, client, new_cocktail):
        """Test deletion of an existing cocktail """
        
        new_cocktail.save()
        latest_cocktail = Cocktail.objects.latest('id')
        url = reverse('api:cocktails-detail', args=[str(latest_cocktail.id)])
        response = client.delete(url, content_type='application/json')
        assert response.status_code == status.HTTP_204_NO_CONTENT