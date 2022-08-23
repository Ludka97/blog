from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.games.views import GameViewSet
from api.auth.views import RegisterView, LoginView
from api.purchase.views import PurchaseView

app_name = "api"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"games", GameViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("purchase/", PurchaseView.as_view(), name="purchase"),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
