def borrow_book(library, book_id):

    for book in library.books:

        if book.book_id == book_id:

            if book.is_borrowed:
                print("Book already borrowed")

            else:
                book.is_borrowed = True
                print("Book borrowed")

            return

    print("Book not found")


def return_book(library, book_id):

    for book in library.books:

        if book.book_id == book_id:

            if not book.is_borrowed:
                print("Book already available")

            else:
                book.is_borrowed = False
                print("Book returned")

            return

    print("Book not found")