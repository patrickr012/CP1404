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
            except:
                file_mark = int(input("Which book would you like to mark as completed? "))

            file_changes = [mark_as_completed(file_mark, base_list)]
            base_list[file_mark] = file_changes[0]

    output_file = open("book_file.csv", "w")
    print(len(base_list))
    base_list_len = len(base_list)
    for i in range(0, base_list_len):
        output_file.write(str(base_list[i]))

    output_file.close()


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
    print(base_list_length)

    for i in range(0, base_list_length):
        print(base_list[i])


def add_book_to_list(base_list):
    try:
        title = input("Title: ")
    except EOFError:
        title = input("Title cannot be blank ")
    try:
        author = input("Author: ")
    except EOFError:
        author = input("Author cannot be blank ")
    try:
        pages = int(input("Pages: "))
    except (ValueError, EOFError):
        print("Invalid input")
        pages = int(input("Pages: "))

    book = [title, author, pages, "R"]
    base_list.append(book)
    print(book)


def mark_as_completed(file_mark, base_list):
    print(base_list[1])


main()
