class Book:
    def __init__(self, title, author):
        self.title = title                # Public attribute
        self.author = author              # Public attribute
        self._is_checked_out = False      # Private attribute for availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Was not checked out

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find a book by title and check it out."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False  # Not found or unavailable

    def return_book(self, title):
        """Find a book by title and return it."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Not found or was not checked out

    def list_available_books(self):
        """Print all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
