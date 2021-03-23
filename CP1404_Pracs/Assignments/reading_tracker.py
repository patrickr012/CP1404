"""
Patrick Robinson
12251568
Menu based program, store book lists in file and modify them when needed.




"""


def main():
    display_book_amount()
    name = input("Please enter your name ")
    print("Welcome {} ".format(name))
    print(MENU)
    input_file = open("book_file.csv", "r")
    base_list = input_file.readlines()
    input_file.close()
    print(base_list)

    menu_choice = input("Please select an option").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            list_all_books(base_list)
            menu_choice = input("Please select an option").upper()
        elif menu_choice == "A":

            add_book_to_list(base_list)
            menu_choice = input("Please select an option").upper()
        elif menu_choice == "M":
            try:

                file_mark = int(input("Which book would you like to mark as completed? "))
                menu_choice = mark_as_completed(base_list, file_mark)
            except IndexError:
                print("Incorrect Index")
                continue

            menu_choice = input("Please select an option").upper()

    output_file = open("book_file.csv", "w")
    print(len(base_list))

    base_list_len = len(base_list)
    for i in range(0, base_list_len):
        output_file.write(str(base_list[i]))

    output_file.close()


def mark_as_completed(base_list, file_mark):
    base_list_length = len(base_list)
    string_list = str(base_list[file_mark])
    string_list.replace("R", "C", -1)
    base_list[file_mark] = string_list

    return base_list


MENU = "Menu: \n" \
       "L - List all books\n" \
       "A - Add new book\n" \
       "M - Mark a book as completed\n" \
       "Q - Quit"

print("Reading Tracker 1.0 - by Patrick Robinson")


def display_book_amount():
    file_length = open("book_file.csv", "r")
    file_length_int = len(file_length.readlines())
    print(" {} books loaded ".format(file_length_int))
    file_length.close()


def list_all_books(base_list):
    base_list.sort()
    base_list_length = len(base_list)
    pages_required = 0
    for i in range(0, base_list_length):
        string_list = str(base_list[i])

        split_list = string_list.split(',')
        title = split_list[0].replace('["', "")
        title[0].replace("[", "")
        author = split_list[1].replace("'", "")
        pages = split_list[2]
        if "R" in split_list[3]:
            print("*", end="")
            pages_required += int(pages)
        print("Title: ", title, end="\t")
        print("Author: ", author, end="\t")
        print("Pages: ", pages)
    print("Pages required: ", pages_required)


def add_book_to_list(base_list):
    while True:

        title = input("Title: ").title()
        if len(title) <= 0:
            title = input("Title cannot be blank ").title()

        author = input("Author: ").title()
        if len(author) <= 0:
            author = input("Author cannot be blank ").title()
        pages = int(input("Pages: "))
        if pages <= 0 or not int:
            print("Invalid input")
            pages = int(input("Pages: "))

        book = [title, author, pages, "R"]
        base_list.append(book)
        print(book)
        break


main()
