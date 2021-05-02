"""
CP1404/CP5632 Practical
Car class
"""
from car import Car


class Taxi(Car):
    PRICE_PER_KM = 1.23
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car.
        :param fuel: float, one unit of fuel drives one kilometer"""
        super().__init__(name, fuel)

        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.PRICE_PER_KM)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return (self.PRICE_PER_KM * self.current_fare_distance).__round__(1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well.
        :param distance: float, the distance the car will drive"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
