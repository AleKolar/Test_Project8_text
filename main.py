
from library import Library, Book, library

if __name__ == "__main__":
    library = Library()

    library.add_book("Book_1", "Fitzgerald", 1900)
    library.add_book("Book_2", "Morrisy", 2000)

    library.remove_book(2)

    library.add_book("Book_3", "H.Derby", 2000)

    library.display_books()

    library.change_status(2, "выдана")

    print("Книги библиотеки:")
    library.display_books()

    book = library.get_book(1)
    if book is not None:
        print(f"Book with ID 3: {book.title}, {book.author}, {book.year}, {book.status}")
    else:
        print("Book with ID 3 not found in the library.")

    for book_id, book in library.books.items():
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")


