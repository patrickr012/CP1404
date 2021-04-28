"""
Patrick Robinson
12251568
Storing and printing the users guitars.
Calculating and displaying the age of the guitars and whether they are vintage.


"""

from guitar import Guitar

guitar_list = []
name = input("Name: ")
guitar_list.append(name)
while name != "":  # Looping until a blank input
    try:
        year = int(input("Year: "))
    except ValueError:
        print("Invalid Input")  # Handling exceptions
    try:
        cost = float(input("Cost: "))
    except ValueError:
        print("Invalid Input")
    guitar_list.append(Guitar(name, year, cost))
    print(name, "(", year, ")", " : ", "$", cost, "added.")  # Confirming the input

    name = input("Name: ")
print("These are my guitars:")
list_length = len(guitar_list)
for i in range(1, list_length):
    print("Guitar ", i, ": ", guitar_list[i])  # Printing all the guitars in a formatted form
