# Base class: Vehicle
class Vehicle:
    def move(self):
        """Base method for movement. To be overridden by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴‍♂️")

# Example usage
def main():
    # List of different vehicle objects
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    # Demonstrate polymorphism
    for vehicle in vehicles:
        vehicle.move()

if __name__ == "__main__":
    main()
