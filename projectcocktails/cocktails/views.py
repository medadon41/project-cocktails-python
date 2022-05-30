from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views import View

from cocktails.forms import CocktailReceiptForm
from cocktails.models import Cocktail, Ingredient


def index(request):
    tutorials = Cocktail.objects.all()

    title = request.GET.get('title', None)
    if title is not None:
        tutorials = tutorials.filter(title__icontains=title).values()

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
            receipt = form.save()
            receipt.author = request.user
            receipt.ingredients.set(form.cleaned_data.get('ingredients'))
            receipt.save()
            request.user.receipts.add(receipt)
            return redirect('index')
        context = {
            "form": form
        }
        return render(request, 'cocktails/create.html', context)


class CocktailUpdateView(View):
    def get(self, request, pk):
        receipt = Cocktail.objects.get(pk=pk)
        form = CocktailReceiptForm(instance=receipt)
        context = {
            "form": form
        }
        return render(request, 'cocktails/edit.html', context)

    def post(self, request, pk):
        receipt = Cocktail.objects.get(pk=pk)
        form = CocktailReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save()
            return redirect('index')
        context = {
            "form": form
        }
        return render(request, 'cocktails/edit.html', context)


class CocktailsView(View):
    def get(self, request):
        receipts = Cocktail.objects.all()

        others = Ingredient.objects.filter(category='OTH')
        lactics = Ingredient.objects.filter(category='MLK')
        fruits = Ingredient.objects.filter(category='FRT')
        vegetables = Ingredient.objects.filter(category='VGT')
        alcohol = Ingredient.objects.filter(category='ALC')
        syrups = Ingredient.objects.filter(category='SRP')
        juices = Ingredient.objects.filter(category='JCE')
        water = Ingredient.objects.filter(category='WTR')

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

    def delete(self, request):
        count = Cocktail.objects.all().delete()
        return HttpResponse({'message': '{} Cocktails were deleted successfully!'.format(count[0])})


class FilteredCocktailsView(View):
    def get(self, request, fltr):
        cocktails = Cocktail.objects.filter(ingredients__name=fltr)
        context = {
            'receipts': cocktails
        }
        return render(request, 'cocktails/index.html', context)


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

