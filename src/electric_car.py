from src.vehicle_pytest import Vehicle


class ElectricCar(Vehicle):
    """Child class representing an electric car."""

    def __init__(self, vehicle_id: int, model: str, battery_percentage: int, maintenance_status: str, rental_price: float, seating_capacity: int) -> None:

        super().__init__(vehicle_id, model, battery_percentage, maintenance_status, rental_price)

        self.seating_capacity = seating_capacity

    def display_details(self) -> None:
        """Display electric car details."""

        print("\nElectric Car")

        super().display_details()

        print(f"Seating Capacity: {self.seating_capacity}"
        )
