from django.shortcuts import render, redirect
from django.http.response import HttpResponse
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
            form.save()
            print('secs')
            return redirect('index')
        context = {
            "form": form
        }
        return render(request, 'cocktails/create.html', context)


class CocktailsView(View):
    def get(self, request):
        receipts = Cocktail.objects.all()

        context = {
            'receipts': receipts,
        }
        return render(request, 'cocktails/index.html', context)

    def delete(self, request):
        count = Cocktail.objects.all().delete()
        return HttpResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])})


class CocktailView(View):
    def get(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        context = {
            'receipt': cocktail,
        }
        return render(request, 'cocktails/receipt.html', context)

    def delete(self, request, pk):
        cocktail = Cocktail.objects.get(pk=pk)
        cocktail.delete()
        return HttpResponse({'message': 'Tutorial was deleted successfully!'})

