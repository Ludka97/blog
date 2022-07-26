from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse
import logging

from posts.models import Post, Address

logger = logging.getLogger(__name__)


def index(request):
    # post_list = Post.objects.all()
    # return HttpResponse(",".join([x.title for x in post_list]))

    if request.GET.get("title"):
        post_list_2 = Post.objects.filter(title__icontains=request.GET.get("title"))
    else:
        post_list_2 = Post.objects.all()
    return HttpResponse(",".join([x.title for x in post_list_2]))

    # logger.info(f"SOME_VAR_ENV:{settings.SOME_VAR_ENV}")
    # if request.GET.get("key") == "test":
    #     return HttpResponse("Posts with test key")
    # incorrect code. Str.16 don't work no matter what number in var "AGE"
    # if request.GET.get("AGE") != 18:
    #     logger.info(f"access:{settings.ALLOWED}")
    # elif request.GET.get("AGE") == 18:
    #     logger.info(f"access:{settings.DENIED}")
    return HttpResponse("Posts index view")


 # searching by GET param

def searching(request):
    if request.GET.get("city"):
        city_list = Address.objects.filter(city__icontains=request.GET.get("city"))
    else:
        city_list = Address.objects.all()
    return HttpResponse(",".join([x.city for x in city_list]))


# function for filter posts by current user

def posts_to_user(request):
    if request.GET.get("post_list"):
        post_list = Post.objects.filter(author_id=request.user)
    else:
        post_list = "Empty"
    return HttpResponse(",".join([x.post for x in post_list]))

# Create your views here.
