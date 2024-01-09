# Create a program which has book and library classes
# User interface for interacting with the system 

class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.ibsn = isbn
        self.publication_year = publication_year
        self.available = True

    
    def __str__(self):
       '''
       This method overrides the special '__str__' method, which is called to create a string representation of the object when it is printed. 
       '''
       return f"'{self.title}' by {self.author}, ISBN: {self.isbn}, Year: {self.publication_year}, Available: {'Yes' if self.available else 'No'}" 

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Book with ISBN {book.isbn} already exists.")
            return
        self.books[book.isbn] = book
        print(f"Book '{book.title}' added successfully.")
    
    def update_book(self, isbn, new_info):
        if isbn not in self.books:
            print("Book not found.")
            return
        self.books[isbn].__dict__.update(new_info)
        print(f"Book with ISBN {isbn} updated.")

    def search_books(self, search_term):
        results = [book for book in self.books.values() if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        if not results:
            print("No books found.")
        for book in results:
            print(book)

    def remove_book(self, isbn):
        if isbn not in self.books:
            print("Book not found.")
            return
        del self.books[isbn]
        print(f"Book with ISBN {isbn} removed.")

def main():
    '''
    This main function is the simple user interface.
    User can add, update, search, remove, or exit the program. 
    '''
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            year = input("Enter publication year: ")
            library.add_book(Book(title, author, isbn, year))
        elif choice == "2":
            isbn = input("Enter ISBN of the book to update: ")
            print("Enter new details (leave blank to skip): ")
            new_title = input("New title: ") or None
            new_author = input("New author: ") or None
            new_year = input("New publication year: ") or None
            new_info = {k: v for k, v in [('title', new_title), ('author', new_author), ('publication_year', new_year)] if v is not None}
            library.update_book(isbn, new_info)
        elif choice == "3":
            search_term = input("Enter search term (title or author): ")
            library.search_books(search_term)
        elif choice == "4":
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()