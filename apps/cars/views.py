from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Car, CarFeature, CarImage
from .serializers import CarFeatureSerializer, CarImageSerializer, CarSerializer


class CarViewSet(ModelViewSet):
    """
    Car ViewSet
    """

    queryset = Car.objects.prefetch_related("features").all()
    serializer_class = CarSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    filterset_fields = ("make", "model", "year", "price", "mileage", "engine_size")
    search_fields = ("make", "model", "year", "price", "mileage", "engine_size")
    ordering_fields = ("year", "price", "mileage", "engine_size")


class CarImageViewSet(ModelViewSet):
    """
    Car Image ViewSet
    """

    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        # Check if the user is the owner of the image
        car_image = self.get_object()
        if car_image.user != request.user:
            return Response(
                {"detail": "You do not have permission to edit this image."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Check if the user is the owner of the image
        car_image = self.get_object()
        if car_image.user != request.user and not request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to delete this image."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


class CarFeatureViewSet(ModelViewSet):
    """
    Car Feature ViewSet
    """

    queryset = CarFeature.objects.all()
    serializer_class = CarFeatureSerializer
