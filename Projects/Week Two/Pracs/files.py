"""
Files
CP1404
Prac Two
Patrick Robinson
12251568

A program designed to read files, output the contents and add the contents together and print them, where possible.


"""


def file_test_1():
    output_file = open("name.txt", "w")
    name_input = input("Please enter your name ")
    output_file.write(name_input)
    output_file.close()


file_test_1()


def file_test_2():
    input_file = open("name.txt", "r")
    for i in input_file:
        print("Your name is : ", i)
    input_file.close()


file_test_2()


def file_test_3():
    global number_input_file
    number_input_file = open("numbers.txt", "r")
    number_total = int(number_input_file.readline()) + int(number_input_file.readline())
    print(number_total)
    number_input_file.close()


file_test_3()


def file_test_4():
    global number_input_file
    number_input_file = open("numbers.txt", "r")
    total_numbers = 0
    for line in number_input_file:
        number = int(line)
        total_numbers += number
    number_input_file.close()
    print("Your total is : ", total_numbers)


file_test_4()
