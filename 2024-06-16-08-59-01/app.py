"""
book:
title
author_name
release_year

print(title)
print(author_name)
print(release_year)

title - author_name - release_year

{title}, by {author} ({year})

List[Books]
Book: title, name, year
{'title': ..., 'name': ..., 'year': ...}
=> List[Dict]

features
add_book
display_books
"""
import colorama
import win11toast
from tkinter import messagebox

colorama.init(autoreset=True)  # Automatically reset color after each print
toast = win11toast.toast

MENU = """
Enter
'a' - add a book
'l': list books
'q': quit
Your choice: """

books = []


def show_error(message):
    messagebox.showerror("Error", message)


def add_book():
    # nguyen van a => Nguyen Van A
    title = input("Enter the book title: ").strip().title()
    author_name = input("Enter the author name: ").strip().title()
    release_year = int(input("Enter the release year: "))

    book: dict = {
        'title': title,
        'author': author_name,
        'year': release_year
    }

    books.append(book)

    toast("Add Book", "Successfully!", on_dismissed=lambda x: None,
          icon=r"C:\Users\ACER\Downloads\Awicons-Vista-Artistic-Coin-add.ico",
          audio=r"C:\Users\ACER\Downloads\Music\Download Free Notification Sound Effects.mp3")


def show_book(book_info: dict) -> None:
    result = f"{book_info['title']}, by {book_info['author']} ({book_info['year']})"
    print(colorama.Fore.GREEN + result)


def display_all_books():
    if len(books) == 0:
        print(colorama.Fore.BLUE + "Empty reading list!")
    else:
        for book in books:
            show_book(book)


# selection = input(MENU)
#
# while selection != 'q':
#     try:
#         if selection == 'a':
#             add_book()
#         elif selection == 'l':
#             display_all_books()
#         else:
#             print("Unknown command, please try again!")
#
#         selection = input(MENU)
#     except Exception as e:
#         print(e)

operations: dict = {
    'a': add_book,
    'l': display_all_books
}

while True:
    try:
        selection = input(MENU)

        if selection in operations:
            operations[selection]()
        elif selection == 'q':
            break
        else:
            print(colorama.Fore.RED + "Unknown command, please try again!")

    except Exception as e:
        show_error(str(e))
