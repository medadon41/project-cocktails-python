from django.urls import path, include
from cocktails import views
from cocktails.views import CocktailsView, CocktailView

urlpatterns = [
    path('', views.index, name="index"),
    path('cocktails/', CocktailsView.as_view()),
    path('cocktails/<int:pk>/', CocktailView.as_view()),
]
