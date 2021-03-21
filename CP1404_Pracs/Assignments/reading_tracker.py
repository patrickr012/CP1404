"""
Patrick Robinson
12251568
Menu based program, store book lists in file and modify them when needed.




"""

INPUT_FILE = "book_file.csv"
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


display_book_amount()
name = input("Please enter your name ")
print("Welcome {} ".format(name))
print(MENU)
menu_choice = input("Please select an option").upper()

if menu_choice == "L":
    book_list = open("book_file.csv", "r")
    book_list.read()
    book_list.close()
    print(MENU)
    menu_choice = input("Please select an option")

elif menu_choice == "A":
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

    book = [title, author, pages, "Required"]
    list_of_books.append(book)
    print(book)
