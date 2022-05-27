from django.contrib import admin

# Register your models here.
from cocktails.models import Cocktail
from ingredients.models import Ingredient

admin.site.register(Cocktail)
admin.site.register(Ingredient)