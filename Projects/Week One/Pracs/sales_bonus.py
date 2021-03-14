"""
CP1404 - Week One
Sales Bonus
A program designed to calculate and display a users bonus based on their input
Patrick Robinson - 12251568


Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.


"""

import math

sales = int(input("Please enter the amount of sales "))  # Getting the amount of sales as a global object

if sales <= 0:
    print("You have entered an incorrect character ")  # Error checking the input
    sales = int(input("Please enter the amount of sales "))


def get_sales_value():  # Getting the value of the sales based on the amount of sales
    for i in range(0, sales, 1):
        sale_value = float(input("Please enter the value of the sales "))
        sale_value += sale_value
    return float(sale_value)


total_sales_value = float(get_sales_value())  # Converting the value into a global float object


def get_bonus_total(): # Calculating and formatting the bonus based on the value of the sales
    if total_sales_value >= 1000:
        print("Your bonus is : $ {:.2f}".format(total_sales_value * 0.15))
    else:
        print("Your bonus is : $ {:.2f} ".format(total_sales_value * 0.10))


get_bonus_total() # Printing the results
print("Your total amount of sales is : ", sales)

print("The value of your sales is : $ ", total_sales_value)
