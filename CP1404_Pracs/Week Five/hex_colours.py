"""
Patrick Robinson
12251568
Hex Colours
Printing the hex code of colours based on user entry



"""

HEX_COLOURS = {"ALICEBLUE": "#f0f8ff", "AZURE1": "#f0ffff", "BEIGE": "#f5f5dc", "BLUE1": "#0000ff",
               "BLUEVIOLET": "#8a2be2", "BROWN": "#a52a2a", "BURLYWOOD": "#deb887", "CADETBLUE": "#5f9ea0",
               "CORAL": "#ff7f50", "DARKGREEN": "#006400"}

print(HEX_COLOURS)

colour_choice = input("Please choose a colour ").upper()
while colour_choice != "":  # Looping until a blank answer is entered
    if colour_choice not in HEX_COLOURS:
        print("Invalid choice")
    else:
        print("{} is {}".format(colour_choice, HEX_COLOURS[colour_choice]))
        colour_choice = input("Please choose a colour ").upper()
