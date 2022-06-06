from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from apps.cocktails.forms import CocktailReceiptForm
from apps.cocktails.models import Cocktail
from apps.ingredients.models import Ingredient
from projectcocktails import settings


class CocktailCreateTestCase(TestCase):
    def setUp(self) -> None:
        Ingredient.objects.create(name='test_ingredient')
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username="testuser", password="12345")

    def test_cocktail_post_valid_form(self):
        form_data = {'name': "test123", "description": "testtest123",
                     'ingredients': [Ingredient.objects.get(name='test_ingredient')]}
        response = self.client.post("/cocktails/create/", data=form_data)

        self.assertEqual(response.status_code, 200)

    def test_cocktail_post_invalid_form(self):
        form_data = {'name': "test123"}
        self.client.post("/cocktails/create/", data=form_data)

        self.assertFalse(Cocktail.objects.filter(name='test123').exists())


class CocktailUpdateTestCase(TestCase):
    def setUp(self) -> None:
        Ingredient.objects.create(name='test_ingredient')
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username="testuser", password="12345")

    def test_cocktail_update(self):
        cocktail = Cocktail.objects.create(name='test123', description="test123123")
        form_data = {'name': "updated_test", "description": "updated_test",
                     'ingredients': [Ingredient.objects.get(name='test_ingredient')]}
        response = self.client.post(f"/cocktails/{cocktail.id}/edit/", data=form_data)
        self.assertEqual(response.status_code, 200)

