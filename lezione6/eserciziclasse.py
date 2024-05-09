#ESERCIZIO 2
"""
class Student:
    def __init__(self, name:str, studyprogram:str, age:int, gender:str) -> None:
        self.name = name
        self.studyprogram = studyprogram
        self.age = age
        self.gender = gender
    
    def printInfo(self) -> str:
        return self.name, self.studyprogram, self.age, self.gender

leonardo : Student = Student(name="Leonardo", studyprogram="Informatic", age=20, gender="ND")
daniele : Student = Student(name="Daniele", studyprogram="Science", age=21, gender="M")
valerio : Student = Student(name="Valerio", studyprogram="Military", age=20, gender="F")

print(leonardo.printInfo())
"""
#ESERCIZIO 3
"""
class Animal:
    def __init__(self, name:str, age:int, legs:int) -> None:
        self.name = name
        self.age = age
        self.legs = legs
    
    def setLegs(self, legs) -> int:
        self.legs = legs
        return self.legs
    
    def getLegs(self, legs)->int:
        return legs

    def printInfo(self)->str:
        print(f"{self.name}, {self.age}, {self.legs}")
        
    
dog : Animal = Animal(name="Wendy", age=2, legs=4)
cat : Animal = Animal(name="Spritz", age=10, legs=4)

legs = input("Inserisci gambe: ")
legs = int(legs)
dog.setLegs(legs)
dog.printInfo()
"""
#ESERCIZIO 4
class Food:
    def __init__(self, name:str, price:int, description:int) -> None:
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self, menu : list = []) -> None:
        self.menu = menu
    
    def addFood(self, menu)->str:
        add = input("Write the food that you want to add: ")
        menu.append(add)
    
    def removeFood(self, menu)-> str:
        print(menu)
        minus = input("Which food do you want to remove?")
        if minus in menu:
            menu.remove(minus)
        

pasta : Food = Food(name="Arrabbiata", price=12, description="Very hot")
pizza : Food = Food(name="Margherita", price=8, description="Classic pizza in Italy")
sweet : Food = Food(name="Tiramisu", price=5, description="Best sweet in the world")
