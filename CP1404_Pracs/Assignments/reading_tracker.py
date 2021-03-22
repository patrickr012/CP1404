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

    menu_choice = input("Please select an option").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            list_all_books()
            menu_choice = input("Please select an option").upper()
        elif menu_choice == "A":

            add_book = str([add_book_to_list()])
            base_list.extend(add_book)
            menu_choice = input("Please select an option").upper()
        elif menu_choice == "M":

            menu_choice = input("Please select an option").upper()
            file_changes = [mark_as_completed()]
            base_list[file_changes[1]] = file_changes[0]

    output_file = open("book_file.csv", "w")
    output_file.writelines(base_list)
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


def list_all_books():
    book_list = open("book_file.csv", "r")
    book_list_input = book_list.readlines()
    book_list_input.sort()
    pages_sum = 0
    for i in range(0, len(book_list_input)):
        title_list = book_list_input[i]
        title_list_x = title_list.split(",")
        if title_list_x[3].count("R") >= 1:
            print("*", i, title_list_x[0], "  by ", end="\t")
        else:
            print(i, title_list_x[0], "  by ", end="\t")

        print(title_list_x[1], end="\t")
        print(title_list_x[2], " pages")
        if title_list_x[3].count("R") >= 1:
            pages_sum += int(title_list_x.pop(2))
    print("Total pages required: ", pages_sum)
    book_list.close()
    print(MENU)


def add_book_to_list():
    get_books = open("book_file.csv", "r")
    list_of_books = []
    for line in get_books:
        list_of_books.append(line)
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
    for i in range(0, len(list_of_books)):
        print(list_of_books[i])
    book = [title, author, pages, "R"]
    list_of_books.append(book)
    print(book)
    get_books.close()
    return list_of_books


def mark_as_completed():
    input_file = open("book_file.csv", "r")
    try:
        file_mark = int(input("Which book would you like to mark as completed? "))
    except ValueError:
        file_mark = int(input("Which book would you like to mark as completed? "))
    required_mark = input_file.readlines()
    print(required_mark[file_mark])
    removing = required_mark[file_mark]
    removing_new = removing.replace('R', '', )
    print(removing_new)
    required_mark[file_mark] = removing_new
    input_file.close()
    return removing_new, file_mark


main()
