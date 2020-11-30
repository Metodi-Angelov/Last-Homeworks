from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    AIR_CON_CUNSUMP = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        total_consumption = (distance * Car.AIR_CON_CUNSUMP) + (distance * self.fuel_consumption)
        if self.fuel_quantity < total_consumption:
            return
        self.fuel_quantity -= total_consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CON_CUNSUMP = 1.6
    LOOSES_FUEL = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        total_consumption = (distance * Truck.AIR_CON_CUNSUMP) + (distance * self.fuel_consumption)
        if self.fuel_quantity < total_consumption:
            return
        self.fuel_quantity -= total_consumption

    def refuel(self, fuel: float):
        total_fuel_to_add = fuel * Truck.LOOSES_FUEL
        self.fuel_quantity += total_fuel_to_add


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)