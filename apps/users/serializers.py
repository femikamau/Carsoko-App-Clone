from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail")

    pictures = serializers.HyperlinkedRelatedField(
        view_name="image-detail", read_only=True, many=True, source="images"
    )

    class Meta:
        model = User
        fields = (
            "id",
            "url",
            "email",
            "first_name",
            "last_name",
            "pictures",
        )
