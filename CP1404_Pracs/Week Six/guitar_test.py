"""
Patrick Robinson
12251568
Testing the functionality of the guitar methods.


"""

from guitar import Guitar

guitar = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)  # Creating the object

print("Age: Expected 98")
print("Age: Got ", guitar.get_age())  # Displaying the accuracy of the methods.
print("Vintage: Expected True")
print("Vintage: Got ", guitar.is_vintage())

print(guitar)
