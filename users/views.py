from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_view(request):
    if request.method == "GET":
        forms = RegisterForm()
        return render(request, "users/register.html", context={"form":forms})
    elif request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.cleaned_data.__delitem__("confirm_password")
            User.objects.create_user(
                **forms.cleaned_data
            )
            return HttpResponse("User created")
        return HttpResponse ("Invalid form")
    

def login_view(request):
    if request.method == "GET":
        forms = LoginForm()
        return render(request, "users/login.html", context={"form": forms})
    elif request.method == "POST":
        forms = LoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(
                username = forms.cleaned_data["username"],
                password = forms.cleaned_data["password"]

            )
            if user is not None:
                login(request, user)
                return HttpResponse("User logged in")
            else:
                forms.add_error(None, "Valid Loggin")
        return render(request, "users/login.html", {"forms": forms})

@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "GET":
        logout(request)
        return HttpResponse("User logged out")