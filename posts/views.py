from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f"SOME_VAR_ENV:{settings.SOME_VAR_ENV}")
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    # incorrect code. Str.16 don't work no matter what number in var "AGE"
    if request.GET.get("AGE") != 18:
        logger.info(f"access:{settings.ALLOWED}")
    elif request.GET.get("AGE") == 18:
        logger.info(f"access:{settings.DENIED}")
    return HttpResponse("Posts index view")


# Create your views here.
