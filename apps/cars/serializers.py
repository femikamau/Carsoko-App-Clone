from rest_framework import serializers

from .models import Car, CarFeature, CarImage


class CarSerializer(serializers.ModelSerializer):
    """
    Car Serializer
    """

    url = serializers.HyperlinkedIdentityField(view_name="car-detail")

    features = serializers.SlugRelatedField(
        slug_field="name",
        read_only=False,
        many=True,
        queryset=CarFeature.objects.all(),
    )

    pictures = serializers.HyperlinkedRelatedField(
        view_name="image-detail",
        read_only=True,
        many=True,
        source="images",
    )

    class Meta:
        model = Car
        fields = (
            "id",
            "url",
            "make",
            "model",
            "year",
            "engine_size",
            "mileage",
            "price",
            "fuel_type",
            "drive_type",
            "transmission",
            "body_type",
            "condition",
            "location",
            "features",
            "pictures",
        )


class CarImageSerializer(serializers.ModelSerializer):
    """
    Car Image Serializer
    """

    url = serializers.HyperlinkedIdentityField(view_name="image-detail")
    car = serializers.HyperlinkedRelatedField(
        view_name="car-detail", read_only=False, queryset=Car.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True)

    class Meta:
        model = CarImage
        fields = ("id", "url", "car", "image", "user")
        read_only_fields = ("user",)


class CarFeatureSerializer(serializers.ModelSerializer):
    """
    Car Feature Serializer
    """

    class Meta:
        model = CarFeature
        fields = ("id", "name")
