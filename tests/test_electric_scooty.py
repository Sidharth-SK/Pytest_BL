import pytest
from src.electric_scooty import ElectricScooty


def test_electric_scooty_creation() -> None:
    """Test ElectricScooty object creation."""

    scooty = ElectricScooty(301, "Ather Rizta", 88, "Good", 450.0, 95)

    assert scooty.vehicle_id == 301
    assert scooty.model == "Ather Rizta"
    assert scooty.get_battery_percentage() == 88
    assert scooty.max_speed_limit == 95