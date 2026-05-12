import pytest
from src.electric_car import ElectricCar


def test_electric_car_creation() -> None:
    """Test ElectricCar object creation."""

    car = ElectricCar(201, "Tata Nexon EV", 90, "Excellent", 2500.0, 5)

    assert car.vehicle_id == 201
    assert car.model == "Tata Nexon EV"
    assert car.get_battery_percentage() == 90
    assert car.seating_capacity == 5