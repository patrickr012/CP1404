"""
Patrick Robinson
12251568


CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    subject_codes = data[0]
    teachers = data[1]
    student_numbers = data[2]
    print(subject_codes)

    for i in range(0, len(data) + 1):
        print("{} is taught by {} and has {} students".format(subject_codes[i], teachers[i], student_numbers[i]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_people = []
    subject_codes = []
    teachers = []
    student_numbers = []
    for line in input_file:
        people = []
        line = line.strip()
        person = line.split(",")

        people += person
        people[2] = int(people[2])
        subject_codes.append(people[0])
        teachers.append(people[1])
        student_numbers.append(people[2])
        list_of_people.append(people)

    input_file.close()
    return subject_codes, teachers, student_numbers


main()
