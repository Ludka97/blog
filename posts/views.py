from django.http import HttpResponse
from django.shortcuts import redirect, render

from posts.forms import PostForm
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})


def post_add(request):
    if not request.user.is_authenticated:
        return HttpResponse("You aren't authenticated!")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(author=request.user, **form.cleaned_data)
            return redirect("index")
    else:
        form = PostForm()
    return render(request, "post_add.html", {"form": form})

    # post_list = Post.objects.all()
    # return HttpResponse(",".join([x.title for x in post_list]))

    # if request.GET.get("title"):
    #     post_list_2 = Post.objects.filter(title__icontains=request.GET.get("title"))
    # else:
    #     post_list_2 = Post.objects.all()
    # return HttpResponse(",".join([x.title for x in post_list_2]))

    # logger.info(f"SOME_VAR_ENV:{settings.SOME_VAR_ENV}")
    # if request.GET.get("key") == "test":
    #     return HttpResponse("Posts with test key")
    # incorrect code. Str.16 don't work no matter what number in var "AGE"
    # if request.GET.get("AGE") != 18:
    #     logger.info(f"access:{settings.ALLOWED}")
    # elif request.GET.get("AGE") == 18:
    #     logger.info(f"access:{settings.DENIED}")
    # return HttpResponse("Posts index view")


# searching by GET param

# def searching(request):
#     if request.GET.get("city"):
#         city_list = Address.objects.filter(city__icontains=request.GET.get("city"))
#     else:
#         city_list = Address.objects.all()
#     return HttpResponse(",".join([x.city for x in city_list]))


# function for filter posts by current user
#
# def posts_to_user(request):
#     if request.GET.get("post_list"):
#         post_list = Post.objects.filter(author_id=request.user)
#     else:
#         post_list = "Empty"
#     return HttpResponse(",".join([x.post for x in post_list]))

# Create your views here.
