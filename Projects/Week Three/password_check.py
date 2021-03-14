"""

Patrick Robinson
12251568
Get password, print asterisks based on length
"""


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Getting password length and printing based on it"""
    password_length = int(len(password))
    print("*" * password_length)


def get_password():
    """Getting password"""
    password = input("Please enter your password ")
    return password


main()
