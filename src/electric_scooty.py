from src.vehicle_pytest import Vehicle


class ElectricScooty(Vehicle):
    """Child class representing an electric scooter."""

    def __init__(self, vehicle_id: int, model: str, battery_percentage: int, maintenance_status: str, rental_price: float, max_speed_limit: int) -> None:

        super().__init__(vehicle_id, model, battery_percentage, maintenance_status, rental_price)

        self.max_speed_limit = max_speed_limit

    def display_details(self) -> None:
        """Display electric scooter details."""

        print("\nElectric Scooter")

        super().display_details()

        print(f"Max Speed Limit: {self.max_speed_limit} km/h"
        )