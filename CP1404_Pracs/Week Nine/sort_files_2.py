"""
Patrick Robinson
12251568
CP1404
"""
import os

directories = {"Docs": [], "Images": [], "Spreadsheets": []}

os.chdir("FilesToSort")

for file in os.listdir("."):  # Looping through all of the files in the directory
    if os.path.isdir(file):
        continue
    extension = file.split(".")[-1]  # Getting the extension from each file
    if extension not in directories:
        extension_choice = input("What category would you like to sort {} into?".format(extension))
        directories[extension] = extension_choice
        try:
            os.mkdir(extension_choice)  # Attempting to make the directories based on the user input
        except FileExistsError:
            pass

        os.rename(file,
                  "{}/{}".format(directories[extension], file))  # Moving the files into the appropriate directories
