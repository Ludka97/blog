from django.urls import include, path
from rest_framework import routers

from api.auth.views import LoginView, RegisterView
from api.games.views import GameViewSet
from api.posts.views import PostViewSet
from api.purchase.views import (
    PopularProductList,
    ProductList,
    ProductPurchaseView,
    PurchaseList,
)

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"games", GameViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("purchase/", PurchaseList.as_view(), name="purchase"),
    path("products/", ProductList.as_view(), name="products"),
    path("products/popular/", PopularProductList.as_view(), name="popular_products"),
    path("products/add/", ProductPurchaseView.as_view(), name="products-add"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
