from rest_framework import serializers
from ingredients.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id',
                  'name',
                  'category',
                  'cocktail')
