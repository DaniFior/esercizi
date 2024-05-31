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

class Member:
    def __init__(self, member_id : int, name : str ) -> None:
        borrowed_books = []
        self.borrowed_books = borrowed_books
        self.member_id = member_id
        self.name = name

    def borrow_book(self, book:Book):
        if book.title not in self.borrowed_books:
            self.borrowed_books.append(book)
    








book1 = Book("La divina commedia", "Dante", 5487)
print(str(book1))