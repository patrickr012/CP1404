"""
CP1404/CP5632 Practical
State names in a dictionary
Printing state names until a blank answer is entered


"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for i in CODE_TO_NAME:  # Iterating through the dictionary
    abbrev = i
    print("{} is {}".format(abbrev, CODE_TO_NAME[abbrev]))

state_code = input("Enter state code: ").upper()  # Printing state based on state code until a blank answer is entered
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid state code")
    state_code = input("Enter state code: ").upper()
