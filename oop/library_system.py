class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for a_book in self.books:
            if isinstance(a_book, EBook):
                print(f"EBook: {a_book.title} by {a_book.author}, File Size: {a_book.file_size}KB")
            elif isinstance(a_book, PrintBook):
                print(f"PrintBook: {a_book.title} by {a_book.author}, Page Count: {a_book.page_count}")
            else:
                print(f"Book: {a_book.title} by {a_book.author}")
