from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UsersAppModelsTestCase(TestCase):
    def test_model_str(self):
        """
        Test that the user string representation is correct
        """
        user = User(
            email="testuser@email.com",
            first_name="Test",
            last_name="User",
            password="testpassword",
        )

        self.assertEqual(str(user), "testuser@email.com")
