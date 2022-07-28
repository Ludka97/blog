from django.db.models import Count
from django.shortcuts import render

from django.http import HttpResponse
from shop.models import Purchase, Product


def products(request):
    product_list = Product.objects.all()
    return HttpResponse(",".join([x.title for x in product_list]))


def product_sorting(request):
    if request.GET.get("cost"):
        product_sorting_list = Product.objects.all().order_by("cost")
    if request.GET.get("cost_sum"):
        product_sorting_list = Product.objects.annotate(purchase_count=Count("purchase__count")*"product__cost").order_by("purchase_count")
    return HttpResponse(",".join([x.title for x in product_sorting_list]))



# Create your views here.
