from django.contrib import admin

from .models import Car, CarFeature, CarImage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "make",
        "model",
        "year",
        "price",
        "created",
        "modified",
    )
    list_filter = (
        "year",
        "created",
        "modified",
    )
    search_fields = (
        "make",
        "model",
        "year",
        "price",
    )
    list_editable = ("price",)
    list_per_page = 25


@admin.register(CarFeature)
class CarFeatureAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created",
        "modified",
    )
    search_fields = ("name",)
    list_per_page = 25


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "car",
        "user",
        "created",
        "modified",
    )
    list_filter = (
        "created",
        "modified",
    )
    search_fields = (
        "car",
        "user",
    )
    list_per_page = 25
