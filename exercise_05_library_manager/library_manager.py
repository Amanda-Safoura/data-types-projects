from collections import Counter
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    category: str
    year: int
    available: bool = True
    
    def __post_init__(self):
        if not self.title or self.year < 0:
            raise ValueError("Veuillez remplir des informations correctes")
    
    @property
    def borrow(self) -> str:
        if self.available:
            self.available = False
            return f"{self.title} borrowed successfully"
        else:
            return f"{self.title} already borrowed"
        
    @property
    def return_book(self) -> str:
        if not self.available:
            self.available = True
            return f"{self.title} returned successfully"
        else:
            return f"{self.title} already present in library"
    

@dataclass
class User:
    name: str
    borrowed_books: list

    def borrow_book(self, library, title):
        
        library_books = library.books
        book_titles = [book.title for book in library_books]
        
        try:
            idx = book_titles.index(title)
            print(title + ' found !')
            # print('Index:' + str(idx))
            
            book = library_books[idx]
            if book.available:
                print('Available')
                print('Currently removing ' + title + ' from ' + library.name + '...')
                book.borrow
                self.borrowed_books.extend([book])
                print(title + ' borrowed by ' + self.name)
                
            else:
                print('Already borrowed')
            
        except ValueError:
            print('This book doesn\'t exist in this library')
            


@dataclass
class Library:
    name: str
    books: list
    
    def add_books(self, book_list) -> None:
        self.books.extend(book_list)

    def search_by_category(self, category) -> list:
        return [book for book in self.books if book.category == category]

    @property
    def statistics(self) -> dict:
        return {
            "total_books" : len(self.books),
            "available" : len([book for book in self.books if book.available]),
            "borrowed" : len([book for book in self.books if not book.available]),
            "categories" : dict(Counter([book.category for book in self.books]))
        }
    
    @property
    def sort_by_year(self) -> list:
        return sorted(self.books, key=lambda b: b.year)


library = Library(
    "My Library",
    []
)

library.add_books([
    Book(
        "Clean Code",
        "Robert Martin",
        "Programming",
        2008
    ),

    Book(
        "Python Crash Course",
        "Eric Matthes",
        "Programming",
        2019
    ),

    Book(
        "A Brief History of Time",
        "Stephen Hawking",
        "Science",
        1988
    ),

    Book(
        "The Pragmatic Programmer",
        "David Thomas",
        "Programming",
        1999
    )
])

search_result = library.search_by_category("Science")
print(search_result)

#borrow Python Crash Course book
print(library.books[1].borrow)
#borrow The Pragmatic Programmer book
print(library.books[3].borrow)

#borrow Clean Code book
print(library.books[0].borrow)
#return Clean Code book
print(library.books[0].return_book)

print(library.statistics)

sorted_library = library.sort_by_year
print(sorted_library)

user = User('Safoura', [])
user.borrow_book(library, "The Pragmatic Programmer")
user.borrow_book(library, "Clean Code")
# print(user.borrowed_books)
# print(library.books)