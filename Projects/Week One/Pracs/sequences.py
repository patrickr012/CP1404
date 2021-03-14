"""
CP1404 - Week One
Sequences
A menu based program designed to calculate and display number sequences.
Patrick Robinson - 12251568



"""

first_number = int(input("Please enter the first number "))
second_number = int(input("Please enter the second number "))

menu_choice = input("Would you like to see the (E)ven numbers, (O)dd numbers or the (S)quares?  Enter Q to quit. ")

if menu_choice == "E":
    for i in range(first_number, second_number, 1):
        if i%2 == 0:
            print(i)
elif menu_choice == "O":
    for i in range(first_number, second_number, 1):
        if i%2 == 1:
            print(i)
elif menu_choice == "S":
    for i in range(first_number, second_number, 1):
        print(i^2)
