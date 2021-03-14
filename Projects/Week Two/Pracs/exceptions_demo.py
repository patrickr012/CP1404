"""
Patrick Robinson
12251568
Testing for exceptions


"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator <= 0:
        print("Invalid number entered ")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

#  When letters or characters are entered
#  When zero is entered as a denominator
#  Yes
