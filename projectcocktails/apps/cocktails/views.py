import asyncio

from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View

from apps.cocktails.forms import CocktailReceiptForm
from apps.cocktails.models import Cocktail, Ingredient

import logging
logger = logging.getLogger(__name__)


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
            receipt = form.save()
            receipt.author = request.user
            receipt.ingredients.set(form.cleaned_data.get('ingredients'))
            receipt.save()
            request.user.receipts.add(receipt)
            context = {
                'receipt': receipt
            }
            logger.info(f'Cocktail #{receipt.id} was created successfully!')
            return render(request, 'cocktails/receipt.html', context)
        context = {
            "form": form
        }
        logger.error('Invalid form')
        return render(request, 'cocktails/create.html', context)


class CocktailUpdateView(View):
    def get(self, request, pk):
        receipt = asyncio.run(get_receipt_by_id_async(pk))
        form = CocktailReceiptForm(instance=receipt)
        context = {
            "form": form
        }
        return render(request, 'cocktails/edit.html', context)

    def post(self, request, pk):
        receipt = asyncio.run(get_receipt_by_id_async(pk))
        form = CocktailReceiptForm(request.POST, request.FILES, instance=receipt)
        if form.is_valid():
            receipt = form.save()
            logger.info(f'Cocktail #{receipt.id} was updated successfully!')
            return redirect('index')
        context = {
            "form": form
        }
        logger.error('Invalid form')
        return render(request, 'cocktails/edit.html', context)


class CocktailsView(View):
    def get(self, request):
        receipts = asyncio.run(get_receipts_async())

        others = asyncio.run(get_ingredients_filtered_async('OTH'))
        lactics = asyncio.run(get_ingredients_filtered_async('MLK'))
        fruits = asyncio.run(get_ingredients_filtered_async('FRT'))
        vegetables = asyncio.run(get_ingredients_filtered_async('VGT'))
        alcohol = asyncio.run(get_ingredients_filtered_async('ALC'))
        syrups = asyncio.run(get_ingredients_filtered_async('SRP'))
        juices = asyncio.run(get_ingredients_filtered_async('JCE'))
        water = asyncio.run(get_ingredients_filtered_async('WTR'))

        context = {
            'receipts': receipts,
            'others': others,
            'lactics': lactics,
            'fruits': fruits,
            'vegetables': vegetables,
            'alcohol': alcohol,
            'syrups': syrups,
            'juices': juices,
            'water': water,
        }
        return render(request, 'cocktails/index.html', context)


class FilteredCocktailsView(View):
    def get(self, request, fltr):
        cocktails = asyncio.run(get_receipts_filtered_async(fltr))
        context = {
            'receipts': cocktails
        }
        return render(request, 'cocktails/index.html', context)


class CocktailView(View):
    def get(self, request, pk):
        cocktail = asyncio.run(get_receipt_by_id_async(pk))
        context = {
            'receipt': cocktail,
        }
        return render(request, 'cocktails/receipt.html', context)

    def delete(self, request, pk):
        cocktail = asyncio.run(get_receipt_by_id_async(pk))
        cocktail.delete()
        return HttpResponse({'message': 'Tutorial was deleted successfully!'})


@sync_to_async
def get_receipt_by_id_async(pk):
    receipt = Cocktail.objects.get(pk=pk)
    return receipt


@sync_to_async
def get_receipts_async():
    receipts = Cocktail.objects.all()
    return receipts


@sync_to_async
def get_receipts_filtered_async(fltr):
    receipts = Cocktail.objects.filter(ingredients__name=fltr)
    return receipts


@sync_to_async
def get_ingredients_filtered_async(fltr):
    ingredients = Ingredient.objects.filter(category=fltr)
    return ingredients
