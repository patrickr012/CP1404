"""
Patrick Robinson
12251568
CP1404
"""
import os
import shutil

os.chdir("FilesToSort")
for source_file in os.listdir("."):  # Looping through all of the files in the directory
    if os.path.isdir(source_file):
        continue

    extension = source_file.split(".")[-1]  # Getting the extension from each file
    print(extensions)
    print(os.getcwd())
    try:
        os.mkdir(extension)  # Attempting to make the directories based on the extensions
    except FileExistsError:
        pass

    print("{}/{}".format(extension, source_file))
    os.rename(source_file, "{}/{}".format(extension, source_file))  # Moving the files into the appropriate directories
