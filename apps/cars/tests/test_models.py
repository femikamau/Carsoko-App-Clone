from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.cars.models import Car, CarFeature, CarImage
from apps.users.tests.data import user_details

from .data import car_details, car_feature_details

User = get_user_model()


class CarsAppModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**user_details)
        self.car_features = CarFeature.objects.bulk_create(
            [CarFeature(**feature) for feature in car_feature_details]
        )
        self.car = Car.objects.create(**car_details)
        self.car_image = CarImage.objects.create(
            car=self.car, image="cars/1.jpg", user=self.user
        )

    def test_model_str(self):
        # Car Model String Representation
        self.assertEqual(
            str(self.car), f"{self.car.year} {self.car.model} {self.car.make}"
        )

        # Car Image Model String Representation
        self.assertEqual(
            str(self.car_image),
            f"{self.car.year} {self.car.model} {self.car.make} Image: {self.car_image.id}",
        )

        # Car Feature Model String Representation
        self.assertEqual(str(self.car_features[0]), car_feature_details[0]["name"])
