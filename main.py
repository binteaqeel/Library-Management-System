from services.library import Library

library = Library()

while True:

    print("\nLibrary System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")
    print("Borrow book huzaifa")
    print("4. Borrow Book by fatima")

    choice = input("Choice: ")

    if choice == "1":

        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")

        library.add_book(book_id, title, author)

    elif choice == "2":

        library.view_books()

    elif choice == "3":
        break