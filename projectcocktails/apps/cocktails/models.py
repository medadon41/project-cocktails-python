from django.db import models
from django.contrib.auth.models import User
from apps.ingredients.models import Ingredient
from projectcocktails import settings
from cloudinary.models import CloudinaryField


class Cocktail(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='receipts')
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=False, default='')
    image = CloudinaryField('image', default='default.png')
    ingredients = models.ManyToManyField(Ingredient)

