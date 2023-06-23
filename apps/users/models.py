from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.utils.models import TimeStampedModel

from .managers import CustomUserManager


class User(PermissionsMixin, AbstractBaseUser, TimeStampedModel):
    """
    A Custom User Model.

    Extends the base Django `AbstractBaseUser`,
    `PermissionsMixin` and a custom `TimeStampedModel`.
    """

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        """
        Return the email of the user as the string representation.
        """
        return self.email
