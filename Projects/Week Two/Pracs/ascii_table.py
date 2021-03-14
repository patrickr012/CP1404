"""
Patrick Robinson
12251568
Checking values of ascii characters



"""
UPPER_LIMIT = 127
LOWER_LIMIT = 33

character = input("Enter a character ")
number = int(input("Enter a number "))

if number > 127 or number < 33:
    print("You have enter an invalid number")
    number = int(input("Enter a number "))

character_ascii = ord(character)
number_ascii = chr(number)

results = "{:<2} {:>2} "
results.split(" : ")
print(results.format(character_ascii, number_ascii))


number = LOWER_LIMIT

for i in range(number, UPPER_LIMIT, 1):
    print(results.format(number, chr(number)) , number+1 , chr(number+1),end="\n")
    number+=2