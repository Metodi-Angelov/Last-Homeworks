from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIR_CON_CUNSUMP = 0.9

    def drive(self, distance):
        total_consumption = (distance * Car.AIR_CON_CUNSUMP) + (distance * self.fuel_consumption)
        if self.fuel_quantity >= total_consumption:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CON_CUNSUMP = 1.6
    LOOSES_FUEL = 0.95

    def drive(self, distance):
        total_consumption = (distance * Truck.AIR_CON_CUNSUMP) + (distance * self.fuel_consumption)
        if self.fuel_quantity >= total_consumption:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        total_fuel_to_add = fuel * Truck.LOOSES_FUEL
        self.fuel_quantity += total_fuel_to_add
