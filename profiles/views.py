from django.shortcuts import render
from django.http import HttpResponse


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


# Create your views here.
