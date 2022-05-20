from rest_framework import serializers
from cocktails.models import Cocktail, Ingredient


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ('id',
                  'name',
                  'description',
                  'published',
                  'ingredients')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id',
                  'name',
                  'category',
                  'cocktail')
