# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        """
        Initialize the Smartphone object with its attributes.
        """
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_capacity = battery_capacity  # in mAh
        self.powered_on = False

    def power_on(self):
        """Turn on the smartphone."""
        if not self.powered_on:
            self.powered_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        """Turn off the smartphone."""
        if self.powered_on:
            self.powered_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def check_storage(self):
        """Display the storage capacity of the smartphone."""
        print(f"{self.brand} {self.model} has {self.storage}GB of storage.")

    def __str__(self):
        return f"{self.brand} {self.model}: {self.storage}GB, {self.battery_capacity}mAh battery"


# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_capacity, gpu, cooling_system):
        """
        Initialize the GamingSmartphone with additional attributes.
        """
        super().__init__(brand, model, storage, battery_capacity)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def activate_game_mode(self):
        """Activate game mode for better performance."""
        if self.powered_on:
            print(f"Game mode activated on {self.brand} {self.model}. Enhanced GPU ({self.gpu}) and cooling system ({self.cooling_system}) engaged!")
        else:
            print("Please power on the smartphone to activate game mode.")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, GPU: {self.gpu}, Cooling: {self.cooling_system}"


# Example usage
if __name__ == "__main__":
    # Create a standard smartphone
    phone1 = Smartphone("Apple", "iPhone 14", 256, 3200)
    print(phone1)
    phone1.power_on()
    phone1.check_storage()
    phone1.power_off()

    print()

    # Create a gaming smartphone
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 512, 6000, "Adreno 730", "Liquid Cooling")
    print(gaming_phone)
    gaming_phone.power_on()
    gaming_phone.activate_game_mode()
    gaming_phone.power_off()
