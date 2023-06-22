from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from apps.cars.views import CarFeatureViewSet, CarImageViewSet, CarViewSet
from apps.users.views import UserViewSet

router = DefaultRouter()

router.register(prefix=r"users", viewset=UserViewSet, basename="user")
router.register(prefix=r"cars", viewset=CarViewSet, basename="car")
router.register(prefix=r"images", viewset=CarImageViewSet, basename="image")
router.register(prefix=r"features", viewset=CarFeatureViewSet, basename="feature")


urlpatterns = [
    path(route="login/", view=obtain_auth_token),
    path("rest-auth/", include("rest_framework.urls")),
] + router.urls
