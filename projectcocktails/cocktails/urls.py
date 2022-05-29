from django.urls import path, include
from cocktails import views
from cocktails.views import CocktailsView, CocktailView, CocktailCreateView, FilteredCocktailsView

urlpatterns = [
    path('', views.index, name="index"),
    path('cocktails/', CocktailsView.as_view(http_method_names=['get'])),
    path('cocktails/create', CocktailCreateView.as_view(), name="create"),
    path('cocktails/<int:pk>/', CocktailView.as_view(http_method_names=['get'])),
    path('cocktails/<str:fltr>/', FilteredCocktailsView.as_view())
]
