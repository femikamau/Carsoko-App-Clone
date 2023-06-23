from django.contrib.auth import get_user_model
from django.test import TestCase

from .data import superuser_details, user_details

User = get_user_model()


class UsersAppManagersTestCase(TestCase):
    def test_create_user(self):
        """
        Test creating a new user
        """
        user = User.objects.create_user(**user_details)

        self.assertEqual(user.email, "testuser@email.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_missing_email(self):
        """
        Test creating a new user with no email raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "email": None})

    def test_create_user_missing_first_name(self):
        """
        Test creating a new user with no first name raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "first_name": None})

    def test_create_user_missing_last_name(self):
        """
        Test creating a new user with no last name raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "last_name": None})

    def test_regular_user_as_staff(self):
        """
        Test creating a new user with is_staff=True raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "is_staff": True})

    def test_regular_user_as_superuser(self):
        """
        Test creating a new user with is_superuser=True raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_user(**{**user_details, "is_superuser": True})

    def test_create_superuser(self):
        """
        Test creating a new superuser
        """
        user = User.objects.create_superuser(**superuser_details)

        self.assertEqual(user.email, "testsuperuser@email.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "Superuser")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_superuser_not_staff(self):
        """
        Test creating a new superuser with is_staff=False raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_superuser(**{**superuser_details, "is_staff": False})

    def test_superuser_not_superuser(self):
        """
        Test creating a new superuser with is_superuser=False raises error
        """
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                **{**superuser_details, "is_superuser": False}
            )
