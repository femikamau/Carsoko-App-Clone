from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    A Custom Admin for the Custom User Model.

    Extends the base Django `UserAdmin`.
    """

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "created",
        "modified",
    )
    list_filter = ("is_staff", "is_active", "created", "modified")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    readonly_fields = ("created", "modified")
    fieldsets = (
        (
            "User",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                    "created",
                    "modified",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
    )
    add_fieldsets = (
        (
            "User",
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
