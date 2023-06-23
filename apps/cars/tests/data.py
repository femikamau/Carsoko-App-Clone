from apps.cars.models import Car

car_feature_details = [
    {"name": "Air Conditioning"},
    {"name": "Airbags"},
    {"name": "Alloy Wheels"},
    {"name": "AM/FM Radio"},
    {"name": "Armrests"},
    {"name": "CD Player"},
    {"name": "Cup Holders"},
]

car_details = {
    "make": "Toyota",
    "model": "Corolla",
    "year": 2019,
    "engine_size": 1800,
    "mileage": 10000,
    "price": 1000000,
    "fuel_type": Car.FuelTypeChoices.PETROL,
    "drive_type": Car.DriveTypeChoices.FOUR_WHEEL_DRIVE,
    "transmission": Car.TransmissionChoices.AUTOMATIC,
    "body_type": Car.BodyTypeChoices.SALOON,
    "condition": Car.ConditionChoices.FOREIGN_USED,
    "location": "Nairobi, Kenya",
}
