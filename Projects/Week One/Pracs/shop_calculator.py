"""
CP1404 - Week One
Shop Calculator
A program designed to calculate the value of a set number of items, output the value and apply a 10% discount
if the total value is greater than 100.
Patrick Robinson - 12251568



"""

import math

number_of_items = int(input("Please enter the number of items "))

if number_of_items <= 0:
    print("You have entered an incorrect character ")  # Error checking the input
    number_of_items = int(input("Please enter the amount of items "))


def get_items_value():  # Getting the value of the items based on the amount of items
    for i in range(0, number_of_items, 1):
        item_value = float(input("Please enter the value of the items "))
        item_value += item_value
    return float(item_value)


total_item_value = float(get_items_value())  # Converting the value into a global float object


def get_discount_total():  # Calculating and formatting the discount based on the value of the items
    if total_item_value >= 100:
        print("Your discount is : $ {:.2f}".format(total_item_value * 0.10))
        print("Your total cost is : $ {:.2f}".format(total_item_value - (total_item_value * 0.10)))
    else:
        print("Your price is too low to receive a discount. ")


get_discount_total()  # Printing the results
print("Your total amount of items is : ", number_of_items)

print("The value of your sales is : $ ", total_item_value)
