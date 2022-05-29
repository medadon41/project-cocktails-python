from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View


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
            form.save()
            return redirect('/cocktails')
        context = {
            "form": form
        }
        return render(request, "auth/register.html", context)
