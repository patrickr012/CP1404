"""
Patrick Robinson
12251568
CP1404
A program designed to drive an unreliable car.  If the cars reliability is less then that of the drive distance the car will not start.
"""

from car import Car
import random


class UnreliableCar(Car):
    """Representing an UnreliableCar object"""

    def __init__(self, name, fuel, reliability=0):
        """Initialising the UnreliableCar object, based on the parent class Car
        :param reliability: float, the reliability of the car, a random number between 0 and 100"""
        super().__init__(name, fuel)
        self.reliablity = 0

    def drive(self, distance):
        """Driving the car a set distance, unless the reliability is less then that of the distance."""
        reliability = random.uniform(0, 100)
        if reliability > distance:

            drive_distance = super().drive(distance)
        else:
            distance = 0
            print("Car broke down")
