from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from apps.cars.models import Car, CarFeature, CarImage
from apps.users.tests.data import superuser_details, user_details

from .data import car_details, car_feature_details

User = get_user_model()


class CarsAppViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**user_details)
        self.superuser = User.objects.create_superuser(**superuser_details)
        self.car_features = CarFeature.objects.bulk_create(
            [CarFeature(**feature) for feature in car_feature_details]
        )
        self.car = Car.objects.create(**car_details)
        self.car_image = CarImage.objects.create(
            car=self.car, image="cars/1.jpg", user=self.user
        )
        self.client = APIClient()

    def test_car_list_view(self):
        # All users and guests should be able to view the list of cars
        response = self.client.get("/apis/cars/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["make"], self.car.make)

    def test_car_detail_view(self):
        # All users and guests should be able to view the details of a car
        response = self.client.get(f"/apis/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["make"], self.car.make)

    def test_car_create_view(self):
        # Guest should not be able to create a car
        response = self.client.post("/apis/cars/", car_details)
        self.assertEqual(response.status_code, 401)

        # Regular User should not be able to create a car
        self.client.login(**user_details)
        response = self.client.post("/apis/cars/", car_details)
        self.assertEqual(response.status_code, 403)

        # Admin User should be able to create a car
        self.client.login(**superuser_details)
        response = self.client.post("/apis/cars/", car_details)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["make"], car_details["make"])

    def test_car_update_view(self):
        # Guest should not be able to update a car
        response = self.client.put(f"/apis/cars/{self.car.id}/", car_details)
        self.assertEqual(response.status_code, 401)

        # Regular User should not be able to update a car
        self.client.login(**user_details)
        response = self.client.put(f"/apis/cars/{self.car.id}/", car_details)
        self.assertEqual(response.status_code, 403)

        # Admin User should be able to update a car
        self.client.login(**superuser_details)
        response = self.client.put(f"/apis/cars/{self.car.id}/", car_details)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["make"], car_details["make"])

    def test_car_delete_view(self):
        # Guest should not be able to delete a car
        response = self.client.delete(f"/apis/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 401)

        # Regular User should not be able to delete a car
        self.client.login(**user_details)
        response = self.client.delete(f"/apis/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 403)

        # Admin User should be able to delete a car
        self.client.login(**superuser_details)
        response = self.client.delete(f"/apis/cars/{self.car.id}/")
        self.assertEqual(response.status_code, 204)

    def test_car_feature_list_view(self):
        # All users and guests should be able to view the list of car features
        response = self.client.get("/apis/features/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 7)
        self.assertEqual(response.data["results"][0]["name"], "Air Conditioning")

    def test_car_feature_detail_view(self):
        # All users and guests should be able to view the details of a car feature
        response = self.client.get(f"/apis/features/{self.car_features[0].id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Air Conditioning")

    def test_car_feature_create_view(self):
        # Guest should not be able to create a car feature
        response = self.client.post("/apis/features/", car_feature_details[0])
        self.assertEqual(response.status_code, 401)

        # Regular User should not be able to create a car feature
        self.client.login(**user_details)
        response = self.client.post("/apis/features/", car_feature_details[0])
        self.assertEqual(response.status_code, 403)

        # Admin User should be able to create a car feature
        self.client.login(**superuser_details)
        response = self.client.post("/apis/features/", car_feature_details[0])
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], car_feature_details[0]["name"])

    def test_car_feature_update_view(self):
        # Guest should not be able to update a car feature
        response = self.client.put(
            f"/apis/features/{self.car_features[0].id}/", car_feature_details[0]
        )
        self.assertEqual(response.status_code, 401)

        # Regular User should not be able to update a car feature
        self.client.login(**user_details)
        response = self.client.put(
            f"/apis/features/{self.car_features[0].id}/", car_feature_details[0]
        )
        self.assertEqual(response.status_code, 403)

        # Admin User should be able to update a car feature
        self.client.login(**superuser_details)
        response = self.client.put(
            f"/apis/features/{self.car_features[0].id}/", car_feature_details[0]
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], car_feature_details[0]["name"])

    def test_car_feature_delete_view(self):
        # Guest should not be able to delete a car feature
        response = self.client.delete(f"/apis/features/{self.car_features[0].id}/")
        self.assertEqual(response.status_code, 401)

        # Regular User should not be able to delete a car feature
        self.client.login(**user_details)
        response = self.client.delete(f"/apis/features/{self.car_features[0].id}/")
        self.assertEqual(response.status_code, 403)

        # Admin User should be able to delete a car feature
        self.client.login(**superuser_details)
        response = self.client.delete(f"/apis/features/{self.car_features[0].id}/")
        self.assertEqual(response.status_code, 204)

    def test_car_image_list_view(self):
        # All users and guests should be able to view the list of car images
        response = self.client.get("/apis/images/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["car"], self.car.id)

    def test_car_image_detail_view(self):
        # All users and guests should be able to view the details of a car image
        response = self.client.get(f"/apis/images/{self.car_image.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["car"], self.car.id)
