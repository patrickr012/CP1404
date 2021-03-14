"""
CP1404 - Week One
Menus
A menu based program designed to output a statement based on a series of choices and test for invalid inputs.
Patrick Robinson - 12251568



"""

name = input("Please enter your name:  ")
print("(H)ello", "\n(G)oodbye", "\n(Q)uit)")
menu_choice = input("Please enter your choice ")

while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello ", name)
    elif menu_choice == "G":
        print("Goodbye ", name)
    else:
        print("Invalid message ")
        print("(H)ello", "\n(G)oodbye", "\n(Q)uit)")
        menu_choice = input("Please enter your choice ")
else:
    print("Finished")



