"""
Patrick Robinson
12251568
Ask for amount of scores and print and write random grades based on input.



"""

import random

output_file = open("results.txt", "w")


def calculate_grade(score):
    """Calculating grade based on score """
    if score < 0:
        return "Invalid Score"
    else:
        if score >= 100:
            return "Invalid Score"
        if score >= 50:
            return "Passable"
        if score >= 90:
            return "Excellent"
        if score < 50:
            return "Bad"


def main():
    score_input = int(input("Please enter number of scores "))
    if score_input > 100 or score_input < 0:
        score_input = int(input("Please try again "))
    for amount in range(0, score_input):
        grade = random.randint(0, 100)
        print(grade, " is ", calculate_grade(grade))
        output_file.write(str(grade))
        output_file.write(" is ")
        output_file.write(calculate_grade(grade))
        output_file.write(".  ")


output_file.close()
main()
