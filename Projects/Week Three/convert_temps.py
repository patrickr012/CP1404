"""
Patrick Robinson
12251568
Get temps in fahrenheit from file, convert to celsius and write back to file.



"""
import random

global fahrenheit_temps
global celsius_temps
fahrenheit_temps = ""
celsius_temps = ""


def generate_fahrenheit_temps():
    """ Getting the fahrenheit temps"""
    global i, fahrenheit_temps
    for i in range(0, 15):
        random_number = random.uniform(-200, 200)
        random_number_str = str(random_number)
        fahrenheit_temps += random_number_str
        fahrenheit_temps += "\n"


generate_fahrenheit_temps()

print(fahrenheit_temps)

output_file = open("temp_inputs.txt", "w")
output_file.write(fahrenheit_temps)
output_file.close()

input_file = open("temp_inputs.txt", "r")


def calculate_celsius_temps():
    """Getting the celsius temps"""
    global i, celsius_temps
    for i in range(0, 15):
        temp_input = input_file.readline().strip()
        temp_input_float = float(temp_input)
        print(temp_input_float)
        print("\n")
        celsius_temp = 5 / 9 * (temp_input_float - 32)
        celsius_temp_str = str(celsius_temp)
        print(celsius_temp_str)
        celsius_temps += celsius_temp_str
        celsius_temps += "\n"


calculate_celsius_temps()

input_file.close()

read_file = open("temp_inputs.txt ", "w")
read_file.write(celsius_temps)
read_file.close()


def convert_to_celsius(line_float):
    """Converting to celsius"""
    celsius_temp = 5 / 9 * (line_float - 32)
    return celsius_temp
