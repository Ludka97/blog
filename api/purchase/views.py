from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.purchase.serializers import ProductSerializer
from shop.models import Product

class PurchaseView(ListAPIView):
    """
    API endpoint that allows get a list of posts.
    """

    queryset = Product.objects.all().order_by("title")
    serializer_class = ProductSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = ProductSerializer(queryset, many=True)
        return Response(queryset.data)

