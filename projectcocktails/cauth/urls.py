from django.urls import path, include
from cauth.views import RegistrationView, ProfileView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('profile/<str:uname>', ProfileView.as_view())
]
