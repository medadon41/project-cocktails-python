from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views import View
from rest_framework import status

from cocktails.forms import CocktailReceiptForm
from cocktails.models import Cocktail
from cocktails.serializers import CocktailSerializer
from rest_framework.decorators import api_view

import json


def index(response):
    tutorials = Cocktail.objects.all()

    title = response.GET.get('title', None)
    if title is not None:
        tutorials = tutorials.filter(title__icontains=title)

    tutorials_serializer = CocktailSerializer(tutorials, many=True)
    return HttpResponse(tutorials_serializer.data)


class CocktailsView(View):
    def get(self, request):
        tutorials = Cocktail.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = CocktailSerializer(tutorials, many=True)
        return HttpResponse(tutorials_serializer.data)

    def post(self, request):
        form = CocktailReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.changed_data.get('image')
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            # ingredients = TODO when frontend

            p = Cocktail.objects.create(name=name, description=description, image=image)
            p.save()
            return redirect('index')

    def delete(self, request):
        count = Cocktail.objects.all().delete()
        return HttpResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class CocktailView(View):
    def get(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail_serializer = CocktailSerializer(cocktail)
        return HttpResponse(json.dumps(cocktail_serializer.data))

    def delete(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail.delete()
        return HttpResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

