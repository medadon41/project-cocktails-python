from django.urls import path, include
from cauth.views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
]
