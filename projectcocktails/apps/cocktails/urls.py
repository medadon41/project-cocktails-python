from django.contrib.auth.decorators import login_required
from django.urls import path, include
from apps.cocktails import views
from apps.cocktails.views import CocktailsView, CocktailView, CocktailCreateView, CocktailUpdateView, FilteredCocktailsView

urlpatterns = [
    path('', CocktailsView.as_view(http_method_names=['get']), name="index"),
    path('cocktails/', CocktailsView.as_view(http_method_names=['get'])),
    path('cocktails/create/', login_required(CocktailCreateView.as_view())),
    path('cocktails/<int:pk>/', CocktailView.as_view(http_method_names=['get'])),
    path('cocktails/<int:pk>/edit/', login_required(CocktailUpdateView.as_view())),
    path('cocktails/<str:fltr>/', FilteredCocktailsView.as_view()),
]
