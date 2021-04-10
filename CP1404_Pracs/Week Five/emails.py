"""
Patrick Robinson
12251568
Emails
Storing the users emails as a key in a dictionary and matching them with the users name.
Printing the results when a blank answer is entered



"""

EMAIL_LIST = {}

email = input("Please enter your email")  # Getting the email
while email != "":

    name = (email.split("@")[0]).title()
    print(name)

    confirm = input("Is your name {}?  (Y/N)".format(name))  # Checking the users name

    if "" in confirm.upper():
        EMAIL_LIST[email] = name
    if "N" in confirm.upper():
        real_name = input("Please enter your name")  # If the name is incorrect, the user may enter the correct one
        EMAIL_LIST[email] = real_name

    email = input("Please enter your email")
    print(EMAIL_LIST.items())  # Printing the items in the dictionary
