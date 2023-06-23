from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .data import superuser_details, user_details

User = get_user_model()


class UsersAppViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**user_details)
        self.superuser = User.objects.create_superuser(**superuser_details)
        self.client = APIClient()

    def test_user_list_view(self):
        # Guest should not be able to view the list of users
        response = self.client.get("/apis/users/")
        self.assertEqual(response.status_code, 401)

        # Regular Users should not be able to view the list of users
        self.client.login(**user_details)
        response = self.client.get("/apis/users/")
        self.assertEqual(response.status_code, 403)

        # Admin Users should be able to view the list of users
        self.client.login(**superuser_details)
        response = self.client.get("/apis/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 2)

    def test_user_detail_view(self):
        # Guest should not be able to view the details of a user
        response = self.client.get(f"/apis/users/{self.user.id}/")
        self.assertEqual(response.status_code, 401)

        # Regular Users should not be able to view the details of a user
        self.client.login(**user_details)
        response = self.client.get(f"/apis/users/{self.user.id}/")
        self.assertEqual(response.status_code, 403)

        # Admin Users should be able to view the details of a user
        self.client.login(**superuser_details)
        response = self.client.get(f"/apis/users/{self.superuser.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], self.superuser.email)
