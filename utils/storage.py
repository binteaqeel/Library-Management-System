import json
from models.book import Book


def save_books(library):

    data = []

    for book in library.books:
        data.append(book.to_dict())

    with open("data/books.json", "w") as file:
        json.dump(data, file, indent=4)


def load_books(library):

    try:

        with open("data/books.json", "r") as file:
            data = json.load(file)

        for item in data:

            book = Book(
                item["book_id"],
                item["title"],
                item["author"]
            )

            book.is_borrowed = item["is_borrowed"]

            library.books.append(book)

    except FileNotFoundError:
        pass