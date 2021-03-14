"""
CP1404 - Week One
Loops
A program designed to test the functionality of various loops.
Patrick Robinson - 12251568





"""

for i in range(1, 21, 2):
    print(i, end=" ")
print()

for i in range(0 , 100, 10):
    print(i, end=" ")
print()


for i in range(20, 1, -1):
    print(i, end=" ")
print()


stars = int(input("Please enter the amount of stars"))
for i in range(1, stars+1, 1):
    print("*" * i, end="\n")
print()