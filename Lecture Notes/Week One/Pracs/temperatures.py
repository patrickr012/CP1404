"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

Patrick Robinson
12251568

"""


def main():
    menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":

            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print("Result: {:.2f} F".format(celsius))

        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()
