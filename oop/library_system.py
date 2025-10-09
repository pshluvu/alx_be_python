# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize a Book with a title and an author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a user-friendly string representation of the Book."""
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook, calling the base class constructor."""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        """Return a string representation for EBook."""
        return f"'{self.title}' by {self.author} (E-Book, {self.file_size}MB)"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook, calling the base class constructor."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation for PrintBook."""
        return f"'{self.title}' by {self.author} (Print Book, {self.page_count} pages)"


class Library:
    def __init__(self):
        """Initialize an empty library (composition)."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)
        print(f"Added {book} to the library.")

    def list_books(self):
        """List all books in the library."""
        print("\nLibrary Collection:")
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(book)
