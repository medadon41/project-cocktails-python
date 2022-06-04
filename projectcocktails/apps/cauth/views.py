from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from apps.cauth.models import Profile


class RegistrationView(View):
    def get(self, request):
        form = UserCreationForm()

        context = {
            "form": form
        }
        return render(request, "auth/register.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('/cocktails')
        context = {
            "form": form
        }
        return render(request, "auth/register.html", context)


class ProfileView(View):
    def get(self, request, uname):
        profile = Profile.objects.get(user__username=uname)
        context = {
            'profile': profile
        }
        return render(request, "auth/profile.html", context)
