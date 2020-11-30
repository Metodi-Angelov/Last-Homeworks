import unittest
from .main import Car
from .main import Truck


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(100, 10)

    def test_refuel(self):
        self.car.refuel(1)
        self.assertEqual(101, 101)

    def test_if_consumption_is_more_than_the_distance(self):
        self.car.drive(100)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_if_consumption_is_less_than_the_distance(self):
        self.car.drive(2)
        self.assertEqual(self.car.fuel_quantity, 78.2)


class TruckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = Truck(200, 20)

    def test_refuel(self):
        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 209.5)

    def test_if_consumption_is_more_than_the_distance(self):
        self.truck.drive(100)
        self.assertEqual(self.truck.fuel_quantity, 200)

    def test_if_consumption_is_less_than_the_distance(self):
        self.truck.drive(1)
        self.assertEqual(self.truck.fuel_quantity, 178.4)


if __name__ == '__main__':
    unittest.main()
