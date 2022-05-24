from rest_framework import serializers
from cocktails.models import Cocktail
from ingredients.models import Ingredient


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ('id',
                  'name',
                  'description',
                  'published',
                  'ingredients')

