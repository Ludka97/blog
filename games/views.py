from django.http import HttpResponse
from django.shortcuts import redirect, render

from games.forms import GameForm
from games.models import Game


def game_add(request):
    if not request.user.is_authenticated:
        return HttpResponse("You aren't authenticated!")

    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            Game.objects.create(user=request.user, **form.cleaned_data)
            return redirect("index")
    else:
        form = GameForm()
    return render(request, "game_add.html", {"form": form})


# Create your views here.
