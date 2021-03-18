"""
Patrick Robinson
12251568

CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]


first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)


first_initials = [name[0] for name in names]
print(first_initials)


full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)


a_names = [name for name in names if name.startswith('A')]
print(a_names)

full_names_lowercase = [i.lower() for i in full_names]
print(full_names_lowercase)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

numbers = [int(i) for i in almost_numbers]
print(numbers)

greater_numbers = [i for i in numbers if i > 9]
print(greater_numbers)
