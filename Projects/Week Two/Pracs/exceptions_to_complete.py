"""


Patrick Robinson
12251568
Testing for exceptions

"""

finished = False
result = 0
while not finished:
    try:
        new_number = int(input(" Please enter a number: "))

        finished = True
    except TypeError:
        print("An error has occurred")

        print("Please enter a valid integer.")

print("Valid result is:", result)
