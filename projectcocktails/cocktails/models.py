from django.db import models

from ingredients.models import Ingredient
from projectcocktails import settings


class Cocktail(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    image = models.ImageField(upload_to=settings.MEDIA_URL, default='default.png', null=False)
    published = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient)

