"""
Patrick Robinson
12251568
Generating random numbers between 0 - 45 , no repeats and presented in a list.


"""

import random

RANDOM_NUMBERS = []
NUMBER_LIST = []


list_amount = int(input("Please enter the amount of lines "))
if list_amount > 7:
    list_amount = int(input("Please enter the amount of lines "))
total_amount = list_amount * 6

while len(RANDOM_NUMBERS) < total_amount:
    number = random.randint(0, 45)
    if RANDOM_NUMBERS.count(number) <= 0:
        RANDOM_NUMBERS.append(number)
    else:
        RANDOM_NUMBERS = []
    NUMBER_LIST = [number for number in RANDOM_NUMBERS]

NUMBER_LIST.sort()

for i in range(0, list_amount):
    print(NUMBER_LIST[i:total_amount:list_amount])
