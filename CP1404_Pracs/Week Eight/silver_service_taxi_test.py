"""
Patrick Robinson
12251568
CP1404
"""

from silver_service_taxi import SilverServiceTaxi

taxi1 = SilverServiceTaxi(name="hummer", fuel=70, fanciness=2)
taxi1.drive(18)
print(taxi1.get_fare())
print(taxi1)
