class Book:
    def __init__(self, title: str, author: str):
        # public attributes
        self.title = title
        self.author = author
        # private attribute tracking checkout state
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned. Return True if successful, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        return not self._is_checked_out

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        # private list of Book instances
        self._books = []

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self._books.append(book)

    def _find_book_by_title(self, title: str):
        # find first book with matching title (case-sensitive)
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title: str):
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.check_out()

    def return_book(self, title: str):
        book = self._find_book_by_title(title)
        if book is None:
            return False
        return book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

