MENU = """
Enter
'a' - add a book
'l': list books
'f': search book
'q': quit
Your choice: """

BOOKS_CSV_FILE_PATH = "csv_files/books.csv"


def get_all_books():
    books: list[dict] = []

    with open(BOOKS_CSV_FILE_PATH) as fo:
        # header row
        headers = next(fo).strip().split(',')

        for line in fo:
            data = line.strip().split(',')
            book = dict(zip(headers, data))
            books.append(book)

    return books


def write_to_csv(books: list[dict]) -> None:
    """
    [
        {
            "book_title": "Conan",
            "author_name": "Gosho",
            "release_year": "1991"
        },
        {
            "book_title": "One Piece",
            "author_name": "Oda",
            "release_year": "1992"
        }
    ]
    """
    headers = list(books[0])

    with open(BOOKS_CSV_FILE_PATH, mode='w') as fw:
        fw.write(','.join(headers) + '\n')
        for book in books:
            data = ','.join(book.values()) + '\n'
            fw.write(data)


def add_book():
    # nguyen van a => Nguyen Van A
    title = input("Enter the book title: ").strip().title()
    author_name = input("Enter the author name: ").strip().title()
    release_year = input("Enter the release year: ")

    book: dict = {
        'title': title,
        'author': author_name,
        'year': release_year
    }

    books = get_all_books()
    books.append(book)
    write_to_csv(books)


def show_book(book_info: dict) -> None:
    result = f"{book_info['title']}, by {book_info['author']} ({book_info['year']})"
    print(result)


def display_all_books():
    books = get_all_books()
    if len(books) == 0:
        print("Empty reading list!")
    else:
        for book in books:
            show_book(book)


def search_by_title():
    books = get_all_books()

    search_title = input("Enter the book title: ").strip().lower()
    not_found = False

    for book in books:
        if search_title in book["title"].lower():
            show_book(book)
            not_found = True

    if not not_found:
        print("Not found!")


operations: dict = {
    'a': add_book,
    'l': display_all_books,
    'f': search_by_title
}


def main():
    while True:
        try:
            selection = input(MENU)

            if selection in operations:
                operations[selection]()
            elif selection == 'q':
                break
            else:
                print("Unknown command, please try again!")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
