from typing import List


"""
Инициализация класса Книга
"""
class Book:
    def __init__(self, id: int, title: str, author: str, year: int):
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = "в наличии"

    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.year})"


"""
Инициализация класса Библиотека, где Библиотека - объект словарь(хранилище) с ключами: атрибуты класса Книга
"""
class Library:
    def __init__(self):
        self.books: dict[int, Book] = {}

    def __str__(self):
        return "\n".join([f"Book {book_id}: {book}" for book_id, book in self.books.items()])

    def save_library_to_file(self, file_name: str) -> None:
        with open(file_name, 'w') as file:
            for book_id, book in self.books.items():
                file.write(f"{book_id},{book.title},{book.author},{book.year},{book.status}\n")

    def load_library_from_file(self, file_name: str,
                               encodings: List[str] = ['utf-8', 'latin1', 'windows-1251']) -> None:
        self.books = {}
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                if not lines:
                    default_book = Book("id","Default Title", "Default Author", 2022)
                    self.books[default_book.id] = default_book
                    self.save_library_to_file(file_name)
                else:
                    for encoding in encodings:
                        try:
                            for line in lines:
                                book_data = line.strip().split(',')
                                book_id, title, author, year, status = book_data
                                self.books[int(book_id)] = Book(title, author, int(year))
                                self.books[int(book_id)].status = status
                            break
                        except UnicodeDecodeError:
                            print(f"Error decoding file with {encoding}. Trying the next encoding...")
                    else:
                        print("Unable to decode the file with the provided encodings.")
        except FileNotFoundError:
            print("File not found. Creating a new library.")


    def get_book(self, book_id): # Отображаем книгу по id (Для визуализации)
        if book_id in self.books:
            book = self.books[book_id]
            print(f"Book ID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Year: {book.year}")
            print(f"Status: {book.status}")
            print(book)
        else:
            print(None)


    """
    Добавляем книгу
    """
    def add_book(self, title: str, author: str, year: int) -> None:
        book_id = len(self.books) + 1
        book = Book(book_id, title, author, year)
        self.books[book_id] = book

    """
    Удаляем книгу
    Я рискну не писать блок try except, так как при работе со словарем, в худшем случае, просто будет выведено "Book not found"
    """
    def remove_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book {book_id} has been removed.")
        else:
            print(f"Book {book_id} not found")

    """
    Ищем книгу по ключам
    """
    def search_book(self, search_term: str) -> List[Book]:
        found_books: List[Book] = []
        book_found: bool = False
        for book_id, book in self.books.items():
            if search_term in [book.title, book.author, str(book.year)]:
                found_books.append(book)
                book_found = True
        if book_found:
            print("Books found!")
            for book in found_books:
                print(f"Found Book: {book.title} by {book.author}")
        else:
            print("No books found.")
        return found_books

    """
    Отображение нашей библиотеки со всеми книгами
    """

    def display_books(self) -> None:
        for book_id, book in self.books.items():
         print(
                f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
            # return book_id, book.title, book.author, book.year, book.status
    """
    Меняем status в логике , либо книга "в наличии", либо её нет, так как она - "выдана"
    """
    def change_status(self, book_id: int, new_status: str) -> None:
        if book_id in self.books:
            current_status: str = self.books[book_id].status
            if current_status == "в наличии" and new_status == "выдана":
                self.books[book_id].status = new_status
            elif current_status == "выдана" and new_status == "в наличии":
                self.books[book_id].status = new_status
            else:
                print("Invalid status change. The book is currently " + current_status)
        else:
            print("Book not found")


library = Library()

file_path = "C:/Users/User/PycharmProjects/Test_Project8_text/my_venv_2/library_data.txt"
library.save_library_to_file(file_path)
library.load_library_from_file(file_path)