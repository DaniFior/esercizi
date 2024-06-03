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
            #print("Libro aggiunto")
        elif book.title in self.borrowed_books:
            print("Libro già presente")

    def return_book(self, book:Book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book)
            #print("Libro rimosso")
        elif book.title not in self.borrowed_books:
            print("Libro non presente")
    
    def __str__(self) -> str:
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_titles})"
    
class Library:
    total_books = 0
    def __init__(self) -> None:
        self.books = []
        self.members = []

    def add_book(self, book:Book):
        self.books.append(book)
        Library.total_books+=1
        #print("Libro aggiunto")
    
    def remove_book(self, book:Book):
        self.books.remove(book)
        Library.total_books-=1
        #print("Libro rimosso")

    def register_member(self, member:Member):
        self.members.append(member)
        #print("Membro aggiunto")

    def lend_book(self, book, member):
        if book in self.books and member in self.members:
            self.books.remove(book)
            member.borrow_book(book)
        else:
            print("Il libro potrebbe non essere disponibile o il membro non è registrato")

    def __str__(self):
        books_str = ([str(book) for book in self.books])
        members_str = ([str(member) for member in self.members])
        return f"Library:\nBooks: {books_str}\nMembers: {members_str}"


book1 = Book("La divina commedia", "Dante", 5487)
book2 = Book("Signore degli anelli", "Totti", 8745)
book3 = Book("Se questo è un uomo", "Primo Levi", 2145)
member1 = Member(101, "Mario")
member2 = Member(666, "Giuseppe")
member3 = Member(874, "Mirko")
member1.borrow_book(book1)
print(str(member1))
print(str(book1))
libreria = Library()
libreria.add_book(book1)
libreria.add_book(book2)
libreria.add_book(book3)
libreria.remove_book(book1)
libreria.register_member(member1)
libreria.register_member(member2)
libreria.register_member(member3)
libreria.lend_book(book2,member2)
libreria.lend_book(book3,member3)
libreria.lend_book(book2, member1)
print(str(libreria))


