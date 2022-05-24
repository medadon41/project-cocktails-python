from django.db import models
from cocktails.models import Cocktail
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    class IngredientCategory(models.TextChoices):
        ALCOHOL = 'ALC', _('Alcohol')
        JUICE = 'JCE', _('Juice')
        SYRUP = 'SRP', _('Syrup')
        LACTIC = 'MLK', _('Lactic')
        WATER = 'WTR', _('Water')
        FRUIT = 'FRT', _('Fruit')
        VEGETABLE = 'VGT', _('Vegetable')
        OTHER = 'OTH', _('Other')

    name = models.CharField(max_length=70, blank=False, default='')
    category = models.CharField(max_length=3, choices=IngredientCategory.choices, blank=False, default=IngredientCategory.OTHER)

    cocktail = models.ForeignKey(Cocktail, related_name='ingredients', on_delete=models.CASCADE, null=True)

    def get_category(self) -> IngredientCategory:
        return self.IngredientCategory(self.category)
