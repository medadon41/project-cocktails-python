from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.cauth.views import RegistrationView

import apps.cocktails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.cauth.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include('apps.cocktails.urls')),
    # path('', include('ingredients.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
