from django import forms
from cocktails.models import Cocktail


class CocktailReceiptForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    name = forms.CharField(widget=forms.TextInput(), required=True)
    description = forms.CharField(widget=forms.Textarea(), required=True)
    ingredients = forms.CharField(widget=forms.TextInput(), required=True)

    class Meta:
        model = Cocktail
        fields = ('image', 'name', 'description', 'ingredients')
