from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from django.views import View
from rest_framework import status

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
        raise NotImplementedError

    def delete(self, request):
        count = Cocktail.objects.all().delete()
        return HttpResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class CocktailView(View):
    def get(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail_serializer = CocktailSerializer(cocktail)
        return HttpResponse(json.dumps(cocktail_serializer.data))

    def post(self, request):
        raise NotImplementedError

    def delete(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail.delete()
        return HttpResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
