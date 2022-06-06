import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.cocktails.models import Cocktail
from apps.ingredients.models import Ingredient

# THE CODE BELOW IS NOT USED


class IngredientsView(View):
    def get(self, request):
        ingredients = Ingredient.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            ingredients = ingredients.filter(title__icontains=title)

        # tutorials_serializer = IngredientSerializer(ingredients, many=True)
        return HttpResponse()

    def post(self, request):
        raise NotImplementedError

    def delete(self, request):
        count = Cocktail.objects.all().delete()
        return HttpResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])})


class IngredientView(View):
    def get(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk)
        #ingredient_serializer = IngredientSerializer(ingredient)
        return HttpResponse()

    def post(self, request):
        raise NotImplementedError

    def delete(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk)
        ingredient.delete()
        return HttpResponse({'message': 'Tutorial was deleted successfully!'})
