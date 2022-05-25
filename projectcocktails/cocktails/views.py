from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views import View

from cocktails.forms import CocktailReceiptForm
from cocktails.models import Cocktail, Ingredient

import json


def index(request):
    tutorials = Cocktail.objects.all()

    title = request.GET.get('title', None)
    if title is not None:
        tutorials = tutorials.filter(title__icontains=title).values()

    print(tutorials)
    return render(request, 'cocktails/index.html')


class CocktailCreateView(View):
    def get(self, request):
        form = CocktailReceiptForm()
        context = {
            "form": form
        }
        return render(request, 'cocktails/create.html', context)

    def post(self, request):
        form = CocktailReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            ingredients_field = []
            image = form.cleaned_data.get('image')
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            ingredients = form.cleaned_data.get('ingredients')

            ingredients_list = list(ingredients.split(';'))

            for ing in ingredients_list:
                i = Ingredient.objects.get_or_create(name=ing)
                ingredients_field.append(i)

            c = Cocktail.objects.create(name=name, description=description, image=image)
            c.ingredients.set(ingredients_field)
            c.save()

        context = {
            "form": form
        }
        return render(request, 'cocktails/create.html', context)


class CocktailsView(View):
    def get(self, request):
        tutorials = Cocktail.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        # tutorials_serializer = CocktailSerializer(tutorials, many=True)
        return render(request)

    def delete(self, request):
        count = Cocktail.objects.all().delete()
        return HttpResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])})


class CocktailView(View):
    def get(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        # cocktail_serializer = CocktailSerializer(cocktail)
        return render(request)

    def delete(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail.delete()
        return HttpResponse({'message': 'Tutorial was deleted successfully!'})

