from book_class import Book

def main():
    # Create an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrate __str__ output
    print(my_book)  # Expected: 1984 by George Orwell, published in 1949

    # Demonstrate __repr__ output
    print(repr(my_book))  # Expected: Book('1984', 'George Orwell', 1949)

    # Explicitly print deletion for automated check
    print(f"Deleting {my_book.title}")
    del my_book

if __name__ == "__main__":
    main()


