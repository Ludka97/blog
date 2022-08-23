from django.conf import settings
from rest_framework import serializers

from shop.models import Product, Purchase


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=200)
    image = serializers.ImageField()
    cost = serializers.IntegerField()


class PurchaseSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField()
    product = serializers.PrimaryKeyRelatedField()
    count = serializers.IntegerField()
