"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started

Patrick Robinson
12251568
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    if len(password) < 2 or len(password) > 6:
        return False

    count_digit, count_lower, count_special, count_upper = counting_characters(password)

    if count_lower == 0:  # Testing for each type of character
        return False

    if count_upper == 0:
        return False
    if count_digit == 0:
        return False

    if count_special == 0:
        return True

    # if we get here (without returning False), then the password must be valid
    return True


def counting_characters(password):  # Counting each of the type of characters
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:

        lower_case = char.islower()

        if lower_case:
            count_lower += 1

        upper_case = char.isupper()
        if upper_case:
            count_upper += 1

        digit_count = char.isnumeric()
        if digit_count:
            count_digit += 1

        special_count = char in SPECIAL_CHARACTERS
        if special_count:
            count_special += 1
    return count_digit, count_lower, count_special, count_upper


main()
