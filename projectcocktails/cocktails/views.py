from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from cocktails.models import Cocktail
from cocktails.serializers import CocktailSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def cocktail_list(request):
    if request.method == 'GET':
        tutorials = Cocktail.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = CocktailSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        cocktail_data = JSONParser().parse(request)
        cocktail_serializer = CocktailSerializer(data=cocktail_data)
        if cocktail_serializer.is_valid():
            cocktail_serializer.save()
            return JsonResponse(cocktail_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(cocktail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Cocktail.objects.all().delete()
        return JsonResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def cocktail_detail(request, pk):
    cocktail = Cocktail.objects.get(pk=pk)
    if request.method == 'GET':
        cocktail_serializer = CocktailSerializer(cocktail)
        return JsonResponse(cocktail_serializer.data)

    elif request.method == 'PUT':
        cocktail_data = JSONParser().parse(request)
        cocktail_serializer = CocktailSerializer(cocktail, data=cocktail_data)
        if cocktail_serializer.is_valid():
            cocktail_serializer.save()
            return JsonResponse(cocktail_serializer.data)
        return JsonResponse(cocktail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # GET / PUT / DELETE tutorial
    elif request.method == 'DELETE':
        cocktail.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def cocktails_list_published(request):
    cocktails = Cocktail.objects.filter(published=True)

    if request.method == 'GET':
        cocktails_serializer = CocktailSerializer(cocktails, many=True)
        return JsonResponse(cocktails_serializer.data, safe=False)
