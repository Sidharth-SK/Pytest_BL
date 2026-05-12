import pytest
from src.vehicle_pytest import Vehicle


def test_vehicle_creation() -> None:
    """Test Vehicle object creation."""

    vehicle = Vehicle(101, "Ather 450X", 85, "Good", 500.0)

    assert vehicle.vehicle_id == 101
    assert vehicle.model == "Ather 450X"
    assert vehicle.get_battery_percentage() == 85
    assert vehicle.get_maintenance_status() == "Good"
    assert vehicle.get_rental_price() == 500.0


def test_valid_battery_percentage() -> None:
    """Test valid battery percentage."""

    vehicle = Vehicle(102, "Ola S1", 60, "Good", 450.0)

    vehicle.set_battery_percentage(95)
    assert vehicle.get_battery_percentage() == 95


def test_invalid_battery_percentage() -> None:
    """Test invalid battery percentage."""

    vehicle = Vehicle(103, "TVS iQube", 70, "Good", 400.0)

    vehicle.set_battery_percentage(150)
    assert vehicle.get_battery_percentage() == 70


@pytest.mark.parametrize("battery_value", [0, 100])
def test_boundary_battery_values(battery_value: int) -> None:
    """Test boundary battery values."""

    vehicle = Vehicle(104, "Simple One", battery_value, "Good", 550.0)
    assert (vehicle.get_battery_percentage() == battery_value)