"""


"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Representing the SilverServiceTaxi object"""

    def __init__(self, fanciness, name, fuel):
        """Initialising the SilverServiceTaxi object
        :param fanciness: float, the fanciness of the taxi, the fanciness multiplies the price_per_km to increase the fare"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.PRICE_PER_KM * float(self.fanciness)
        self.flagfall = 4.50
        self.current_fare_distance = 0
        super().get_fare()

    def __str__(self):
        return f"{self.name}, fuel= {self.fuel}, odo={self.odometer} {self.current_fare_distance}km on current fare, ${self.price_per_km}/km plus flagfall of ${self.flagfall}"

    def get_fare(self):
        fare = super().get_fare()
        total_fare = fare + self.flagfall
        return total_fare
