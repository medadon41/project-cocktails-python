from django.db import models
from django.contrib.auth.models import User
from ingredients.models import Ingredient
from projectcocktails import settings


class Cocktail(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='receipts')
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    image = models.ImageField(upload_to="images/", default='default.png', null=False)
    ingredients = models.ManyToManyField(Ingredient)

