"""
Patrick Robinson
12251568
Testing the functionality of the ProgrammingLanguage class and its methods.


"""

from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)  # Creating the objects
print(ruby)

language_list = [ruby, python, visual_basic]

print("The dynamically typed languages are:")  # Testing whether the objects are dynamically typed
for element in language_list:
    if element.is_dynamic() == "True":
        print(element.name)
