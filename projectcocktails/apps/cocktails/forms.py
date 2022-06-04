from django import forms
from apps.cocktails.models import Cocktail
from apps.ingredients.models import Ingredient


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class CocktailReceiptForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = ('image', 'name', 'description', 'ingredients')

    image = forms.ImageField(required=False)
    name = forms.CharField(widget=forms.TextInput(), required=True)
    description = forms.CharField(widget=forms.Textarea(), required=True)
    ingredients = CustomMMCF(
        queryset=Ingredient.objects.all(),
        widget=forms.SelectMultiple(),
        to_field_name="name",
    )


