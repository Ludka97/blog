from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    return HttpResponse("Posts index view")


# Create your views here.
