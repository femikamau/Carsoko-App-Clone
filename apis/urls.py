from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet

router = DefaultRouter()

router.register(prefix=r"users", viewset=UserViewSet, basename="user")

urlpatterns = [
    path(route="login/", view=obtain_auth_token),
    path("rest-auth/", include("rest_framework.urls")),
] + router.urls
