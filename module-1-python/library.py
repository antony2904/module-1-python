#Classes & Methods:
#Create a class Library that allows you to:
#1.Add books (title and author).
#2.Display all books.
#3.Search for a book by title


class Book:

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def get_info(self):
    return f"'{self.title}' by {self.author}"


class Library:

  def __init__(self):
    self.books = []

  def add_book(self, title, author):
    new_book = Book(title, author)
    self.books.append(new_book)
    print(f"Book added: {new_book.get_info()}")

  def display_books(self):
    if len(self.books) == 0:
      print("Library is empty.")
      return

    print("\n--- All Books in Library ---")
    for i in range(len(self.books)):
      book = self.books[i]
      print(f"{i + 1}. {book.get_info()}")

  def search_book(self, title):
    found = False
    print(f"\nSearching for '{title}':")

    for book in self.books:
      if book.title.lower() == title.lower():
        print(f"Match found -> {book.get_info()}")
        found = True
        break

    if not found:
      print("Book not found in library.")



lib = Library()

lib.add_book("Clean Code", "Robert C. Martin")
lib.add_book("Fluent Python", "Luciano Ramalho")
lib.add_book("The Pragmatic Programmer", "Andy Hunt")

lib.display_books()

lib.search_book("Fluent Python")
lib.search_book("Unknown Book")