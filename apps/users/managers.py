from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    A Custom Manager for the Custom User Model.
    """

    def _create_user(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError("The Email must be set")

        if not first_name:
            raise ValueError("The First Name must be set")

        if not last_name:
            raise ValueError("The Last Name must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)

        if extra_fields.get("is_superuser"):
            raise ValueError("Regular users must have is_superuser=False.")

        if extra_fields.get("is_staff"):
            raise ValueError("Regular users must have is_staff=False.")

        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )

    def create_superuser(
        self, email: str, first_name: str, last_name: str, password: str, **extra_fields
    ):
        """
        Creates and saves a superuser with the given email, first name, last name
        and password.
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
