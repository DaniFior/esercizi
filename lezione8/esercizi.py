#ESERCIZIO 1

from abc import ABC, abstractmethod
'''
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class circle(Shape):

    def __init__(self, raggio:float) -> None:
        self.raggio = raggio

    def area(self):
        return round(3.14 * self.raggio ** 2)
    
    def perimeter(self):
        return round(2 * 3.14 * self.raggio)
    
class rectangle(Shape):

    def __init__(self, base:float, altezza:float) -> None:
        self.altezza = altezza
        self.base = base

    def area(self):
        return self.base*self.altezza
    
    def perimeter(self):
        return self.base*2+self.altezza*2
    
circle1 = circle(5)
rectangle1 = rectangle(10, 5)

print(circle1.perimeter(), circle1.area())
print(rectangle1.perimeter(), rectangle1.area())
'''
#ESERCIZIO 2
'''
class MathOperations():
    
    def sum(x,y):
        return x+y

    def product(x,y):
        return x*y

MathOperations.sum = staticmethod(MathOperations.sum)
MathOperations.product = staticmethod(MathOperations.product)
print(f"Somma: {MathOperations.sum(10,5)}, prodotto: {MathOperations.product(5,5)}")
'''
#ESERICIZIO 3 DA FINIRE

class Book:
    def __init__(self, title, author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f'The title is {self.title}, the author is {self.author} and the ISBN is {self.isbn}'

    def __repr__(self) -> str:
        return f'The title is {self.title}, the author is {self.author} and the ISBN is {self.isbn}'
    
class Member:
    def __init__(self, member_id : int, name : str ) -> None:
        borrowed_books = []
        self.borrowed_books = borrowed_books
        self.member_id = member_id
        self.name = name
        titoli = []
        self.titoli = titoli

    def borrow_book(self, book:Book):
        if book.title not in self.borrowed_books:
            self.borrowed_books.append(book)
            print("Libro aggiunto")
        elif book.title in self.borrowed_books:
            print("Libro già presente")

    def return_book(self, book:Book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book)
            print("Libro rimosso")
        elif book.title not in self.borrowed_books:
            print("Libro non presente")
        
    def salvatitoli(self, book:Book, borrowed_books, titoli):
        for i in borrowed_books:
            titoli.append(book.title)

    def __str__(self) -> str:
        return f'Member {self.name} has code {self.member_id} and this are the borrowed book {self.titoli}'

    @classmethod
    def from_string(cls, string):
        return cls(string=string)
    
class Library:
    def __init__(self, books, members, total_books) -> None:
        self.books = books
        members = []
        self.members = members
        self.total_books = total_books
        library = []
        self.library = library 
    
    def add_book(self, book:Book, library, total_books):
        if book.title not in library: 
            library.append(book.title)
            total_books+=1
        elif book.title in library: 
            print("Libro già presente")
    
    def remove_book(self, book:Book, library, total_books):
        if book.title in library:
            library.remove(book.title)
            total_books-=1
            print("Libro rimosso")
        elif book.title not in library:
            print("Libro non presente in libreria")

    def register_member(self, member:Member, members):
        if member.name not in members:
            members.append(member.name)
            print("Membro aggiunto")
        elif member.name in members:
            print("Membro già nell'elenco")


book1 = Book("La divina commedia", "Dante", 5487)
member1 = Member(101, "Mario")
member1.borrow_book(book1)
print(str(member1))
print(str(book1))