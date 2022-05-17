from django.db import models


class Cocktail(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    type = models.CharField(max_length=200, blank=False, default='')