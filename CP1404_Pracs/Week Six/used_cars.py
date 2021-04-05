"""CP1404/CP5632 Practical - Client code to use the Car class.
Patrick Robinson
12251568

"""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""

    toyota = Car(name="Toyota")  # Using custom names for different cars
    toyota.add_fuel(319)
    toyota.drive(277)
    print(toyota)

    print("fuel =", toyota.fuel)
    print("odo =", toyota.odometer)
    print(toyota)

    print("Car {}, {}".format(toyota.fuel, toyota.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=toyota))  # Different types of formatting

    limo = Car(name="limo")
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)  # Testing the drive function when fuel is inadequate
    print(limo)

    mazda = Car(name="Mazda")
    mazda.add_fuel(50)
    mazda.drive(23)
    print(mazda)


main()
