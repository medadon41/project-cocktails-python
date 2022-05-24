from django.urls import path, include
from ingredients import views
from ingredients.views import IngredientsView, IngredientView

urlpatterns = [
    path('ingredients/', IngredientsView.as_view()),
    path('ingredients/<int:pk>/', IngredientView.as_view()),
]