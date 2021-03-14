"""
Patrick Robinson
12251568
Get temps in fahrenheit from file, convert to celsius and write back to file.



"""
import random

global FAHRENHEIT_TEMPS
global CELSIUS_TEMPS
FAHRENHEIT_TEMPS = ""
CELSIUS_TEMPS = ""


def generate_fahrenheit_temps():
    """ Getting the fahrenheit temps"""
    global i, FAHRENHEIT_TEMPS
    for i in range(0, 15):
        random_number = random.uniform(-200, 200)
        random_number_str = str(random_number)
        FAHRENHEIT_TEMPS += random_number_str
        FAHRENHEIT_TEMPS += "\n"


generate_fahrenheit_temps()

print(FAHRENHEIT_TEMPS)

output_file = open("temp_inputs.txt", "w")
output_file.write(FAHRENHEIT_TEMPS)
output_file.close()

input_file = open("temp_inputs.txt", "r")


def calculate_celsius_temps():
    """Getting the celsius temps"""
    global i, CELSIUS_TEMPS
    for i in range(0, 15):
        temp_input = input_file.readline().strip()
        temp_input_float = float(temp_input)
        print(temp_input_float)
        print("\n")
        celsius_temp = 5 / 9 * (temp_input_float - 32)
        celsius_temp_str = str(celsius_temp)
        print(celsius_temp_str)
        CELSIUS_TEMPS += celsius_temp_str
        CELSIUS_TEMPS += "\n"


calculate_celsius_temps()

input_file.close()

read_file = open("temp_inputs.txt ", "w")
read_file.write(CELSIUS_TEMPS)
read_file.close()


def convert_to_celsius(line_float):
    """Converting to celsius"""
    celsius_temp = 5 / 9 * (line_float - 32)
    return celsius_temp
