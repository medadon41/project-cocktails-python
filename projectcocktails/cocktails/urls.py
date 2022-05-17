from django.urls import path, include
from cocktails import views

urlpatterns = [
    path('cocktails/', views.cocktail_list),
    path('cocktails/<int:pk>/', views.cocktail_detail),
]
