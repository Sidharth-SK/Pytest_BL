class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, vehicle_id: int, model: str, battery_percentage: int, maintenance_status: str, rental_price: float) -> None:
        self.vehicle_id = vehicle_id
        self.model = model

        #Private Attributes
        self.__battery_percentage = 0
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

        self.set_battery_percentage(battery_percentage)


    # Getter Methods
    def get_battery_percentage(self) -> int:
        """Return battery percentage."""

        return self.__battery_percentage

    def get_maintenance_status(self) -> str:
        """Return maintenance status."""

        return self.__maintenance_status

    def get_rental_price(self) -> float:
        """Returns rental price."""

        return self.__rental_price

    # Setter Methods
    def set_battery_percentage(self, battery_percentage: int) -> None:
        """Set battery percentage with validation."""

        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage

        else:
            print("Battery percentage must be between 0 and 100.")

    def set_maintenance_status(self, maintenance_status: str) -> None:
        """Set maintenance status."""

        self.__maintenance_status = maintenance_status

    def set_rental_price(self, rental_price: float) -> None:
        """Set rental price."""

        self.__rental_price = rental_price

    def display_details(self) -> None:
        """Display vehicle details."""

        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Model: {self.model}")
        print(f"Battery Percentage : {self.__battery_percentage}%")
        print(f"Maintenance Status : {self.__maintenance_status}")
        print(f"Rental Price: ₹{self.__rental_price:.2f}")