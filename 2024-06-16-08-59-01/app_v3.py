import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import csv


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


BOOKS_CSV_FILE_PATH = resource_path("csv_files/books.csv")


def get_all_books():
    """Reads all books from the CSV file and returns a list of dictionaries."""
    books = []
    try:
        with open(BOOKS_CSV_FILE_PATH, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append(row)
    except FileNotFoundError:
        # Handle case where file doesn't exist yet (e.g., on first run)
        pass
    return books


def write_to_csv(books):
    """Writes the list of books to the CSV file."""
    with open(BOOKS_CSV_FILE_PATH, "w", newline="") as csvfile:
        fieldnames = books[0].keys() if books else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)


class BookManagerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Book Manager")
        self.root.iconbitmap(resource_path("icons/Messbook-Outdated-Book.ico"))

        # Book List Display
        self.book_list = ttk.Treeview(root, columns=("Title", "Author", "Year"), show="headings")
        self.book_list.heading("Title", text="Title")
        self.book_list.heading("Author", text="Author")
        self.book_list.heading("Year", text="Year")
        self.book_list.pack(pady=10, fill=tk.BOTH, expand=True)

        # Input Frame
        input_frame = ttk.LabelFrame(root, text="Add Book")
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = ttk.Entry(input_frame)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = ttk.Entry(input_frame)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Year:").grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = ttk.Entry(input_frame)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(input_frame, text="Add Book", command=self.add_book).grid(row=3, columnspan=2, pady=10)

        # Search Bar
        ttk.Label(root, text="Search by Title:").pack(pady=5)
        self.search_entry = ttk.Entry(root)
        self.search_entry.pack()
        ttk.Button(root, text="Search", command=self.search_book).pack(pady=5)

        # Refresh Button
        ttk.Button(root, text="Refresh List", command=self.refresh_book_list).pack(pady=5)

        self.refresh_book_list()

    def add_book(self):
        title = self.title_entry.get().strip().title()
        author = self.author_entry.get().strip().title()
        try:
            year = int(self.year_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid year. Please enter a number.")
            return

        book = {'title': title, 'author': author, 'year': year}
        books = get_all_books()
        books.append(book)
        write_to_csv(books)
        self.refresh_book_list()

        # Clear input fields after adding
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)

    def refresh_book_list(self):
        for item in self.book_list.get_children():
            self.book_list.delete(item)

        books = get_all_books()
        for book in books:
            self.book_list.insert("", tk.END, values=(book['title'], book['author'], book['year']))

    def search_book(self):
        search_term = self.search_entry.get().strip().lower()
        books = get_all_books()
        matching_books = [book for book in books if search_term in book['title'].lower()]

        # Clear existing items in the Treeview
        for item in self.book_list.get_children():
            self.book_list.delete(item)

        # Insert matching books
        for book in matching_books:
            self.book_list.insert("", tk.END, values=(book['title'], book['author'], book['year']))


if __name__ == "__main__":
    root = tk.Tk()
    app = BookManagerApp(root)
    root.mainloop()
