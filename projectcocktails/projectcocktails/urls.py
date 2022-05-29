from django.contrib import admin
from django.urls import path, include
from cauth.views import RegistrationView

import cocktails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cauth.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include('cocktails.urls')),
    path('', include('ingredients.urls')),
]
