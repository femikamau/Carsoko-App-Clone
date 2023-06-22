from django.contrib.auth import get_user_model
from django.db import models

from apps.utils.models import TimeStampedModel

User = get_user_model()


class CarFeature(TimeStampedModel):
    """
    Car Feature Model
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


class Car(TimeStampedModel):
    """
    Car Model
    """

    # Choices

    class FuelTypeChoices(models.TextChoices):
        """
        Fuel Type Choices
        """

        PETROL = "petrol", "Petrol"
        DIESEL = "diesel", "Diesel"
        ELECTRIC = "electric", "Electric"
        HYBRID = "hybrid", "Hybrid"

    class DriveTypeChoices(models.TextChoices):
        """
        Drive Type Choices
        """

        FOUR_WHEEL_DRIVE = "4wd", "4 Wheel Drive"
        TWO_WHEEL_DRIVE = "2wd", "2 Wheel Drive"

    class TransmissionChoices(models.TextChoices):
        """
        Transmission Choices
        """

        AUTOMATIC = "automatic", "Automatic"
        MANUAL = "manual", "Manual"

    class BodyTypeChoices(models.TextChoices):
        """
        Body Type Choices
        """

        SUV = "suv", "SUV"
        SALOON = "saloon", "Saloon"
        HATCHBACK = "hatchback", "Hatchback"
        PICKUP = "pickup", "Pickup"
        BTV = "btv", "Buses, Taxis and Vans"
        STATION_WAGON = "station wagon", "Station Wagon"

    class ConditionChoices(models.TextChoices):
        """
        Condition Choices
        """

        NEW = "new", "New"
        FOREIGN_USED = "foreign used", "Foreign Used"
        LOCALLY_USED = "locally used", "Locally Used"

    # Fields

    make = models.CharField(max_length=255, blank=False)

    model = models.CharField(max_length=255, blank=False)

    year = models.IntegerField(null=False)

    engine_size = models.IntegerField()

    mileage = models.IntegerField()

    price = models.IntegerField()

    fuel_type = models.CharField(
        max_length=255, choices=FuelTypeChoices.choices, blank=False
    )

    drive_type = models.CharField(
        max_length=255, choices=DriveTypeChoices.choices, blank=False
    )

    transmission = models.CharField(
        max_length=255, choices=TransmissionChoices.choices, blank=False
    )

    body_type = models.CharField(
        max_length=255, choices=BodyTypeChoices.choices, blank=False
    )

    condition = models.CharField(
        max_length=255, choices=ConditionChoices.choices, blank=False
    )

    location = models.CharField(max_length=255)

    features = models.ManyToManyField(CarFeature, related_name="cars", blank=True)

    def __str__(self):
        return f"{self.year} {self.model} {self.make}"


class CarImage(TimeStampedModel):
    """
    Car Image Model
    """

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")

    image = models.ImageField(upload_to="cars")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return f"{self.car.year} {self.car.model} {self.car.make} Image: {self.id}"

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
