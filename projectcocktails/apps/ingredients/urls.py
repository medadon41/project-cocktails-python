from django.urls import path, include
from apps.ingredients import views
from apps.ingredients.views import IngredientsView, IngredientView

urlpatterns = [
    path('ingredients/', IngredientsView.as_view()),
    path('ingredients/<int:pk>/', IngredientView.as_view()),
]