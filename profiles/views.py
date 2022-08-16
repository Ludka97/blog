from http.cookiejar import logger
from django.shortcuts import render, redirect
from django.http import HttpResponse
from profiles.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            # logger.info(form.cleaned_data["first_name"])
            # logger.info(form.cleaned_data["last_name"])
            # logger.info(form.cleaned_data["email"])`
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse('BadRequest', status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


def profiles(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Profiles with test key")
    elif request.GET.get("name") == "Ludka":
        return HttpResponse("Profiles with names")
    elif request.GET.get("email") == "ludkakachan@gmail.com":
        return HttpResponse("Profiles with email")
    elif request.POST.get("name") != "Ludka":
        return HttpResponse("Post method")
    return HttpResponse("Profiles index view")

#
#


# Create your views here.
