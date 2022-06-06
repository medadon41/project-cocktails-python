from django.contrib import admin

# Register your models here.
from apps.cocktails.models import Cocktail
from apps.ingredients.models import Ingredient

admin.site.register(Cocktail)
admin.site.register(Ingredient)