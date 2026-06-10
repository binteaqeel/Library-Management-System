from models.book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)

    def view_books(self):

        if not self.books:
            print("No books available")
            return

        for book in self.books:

            status = "Borrowed" if book.is_borrowed else "Available"

            print(
                f"{book.book_id} | "
                f"{book.title} | "
                f"{book.author} | "
                f"{status}"
            )