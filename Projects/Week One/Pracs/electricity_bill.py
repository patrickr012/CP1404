"""
CP1404 - Week One
Electricity Bill
A program designed to take in price per kwh in cents, daily use in kwh and number of days in the billing period
and output an estimated bill, based on the users tariff.
Patrick Robinson - 12251568



"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


print("Electricity bill estimator ")
cents_per_kwh = float(input(" Please enter cents per kwh : "))
daily_use_kwh = float(input(" Please enter the daily use in kwh : "))
number_of_days = float(input(" Please enter the number of days in the billing period :"))
tariff = input("Please enter your tariff: ")

if tariff == "11":
    print("Your bill is : $", cents_per_kwh * daily_use_kwh * number_of_days * TARIFF_11)
elif tariff == "31":
    print("Your bill is : $", cents_per_kwh * daily_use_kwh * number_of_days *
          TARIFF_31)
else:
    print("Invalid Input")

