from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
