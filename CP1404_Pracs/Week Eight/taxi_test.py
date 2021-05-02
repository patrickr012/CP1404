"""
Patrick Robinson
12251568
CP1404
Program to demonstrate Class Inheritance, by driving a test taxi.
"""

from taxi import Taxi

test_taxi = Taxi(fuel=100, name="Prius 1")

test_taxi.drive(40)

print(test_taxi)
test_taxi.start_fare()
test_taxi.drive(100)
print(test_taxi)

print(test_taxi.get_fare())
