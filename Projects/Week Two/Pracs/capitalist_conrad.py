"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)

Patrick Robinson
12251568
"""
import random

MAX_INCREASE = random.uniform(0, 1)  # 0%-10%
MAX_DECREASE = random.uniform(0, -1)  # 0%--10%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 1.0
INITIAL_DAYS = 1
OUTPUT_FILE = open("share data.txt", "w")

price = INITIAL_PRICE
OUTPUT_FILE.write("Starting Price is: 1.0")
OUTPUT_FILE.write("${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    INITIAL_DAYS += 1
    OUTPUT_FILE.write("On Day ")
    OUTPUT_FILE.write(str(INITIAL_DAYS))  # Formatting the output and writing it to the appropriate file
    OUTPUT_FILE.write(" the price is : ")

    OUTPUT_FILE.write("${:,.2f}".format(price))

OUTPUT_FILE.close()
