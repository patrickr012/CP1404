"""
Patrick Robinson
12251568
Generating random numbers between 0 - 45 , no repeats and presented in a list.
Week Four


"""

import random

raw_numbers = []

list_amount = int(input("Please enter the amount of lines "))
if list_amount > 7:
    list_amount = int(input("Please enter the amount of lines "))
total_amount = list_amount * 6

while len(raw_numbers) < total_amount:
    number = random.randint(0, 45)
    if raw_numbers.count(number) <= 0:
        raw_numbers.append(number)
    else:
        raw_numbers = []

raw_numbers.sort()

for i in range(0, list_amount):
    print(raw_numbers[i:total_amount:list_amount])
