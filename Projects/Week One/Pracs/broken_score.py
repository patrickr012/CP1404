"""
CP1404/CP5632 - Practical
Broken program to determine score status
Patrick Robinson
12251568



"""
import random


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
    score = float(input("Enter score: "))
    print(calculate_grade(score), score)
    second_score = random.randint(0, 100)
    print(calculate_grade(second_score), second_score)


main()
