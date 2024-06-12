from abc import ABC, abstractmethod

class Forma(ABC):

    def __init__(self, nome) -> None:
        self.nome = nome

    @abstractmethod
    def getArea(self):
        pass

    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato) -> None:
        super().__init__("Quadrato")
        self.lato = lato

    def getArea(self):
        return self.lato*self.lato
    
    def render(self):
        if self.lato < 2:
            for i in range(self.lato):
                print("*", end=" ")
            print()
        else:
            for i in range(self.lato):
                if i == 0 or i == self.lato - 1:
                    print("* "*self.lato)
                else: 
                    print("* "+" "*(self.lato-2)+"*")

quadrato = Quadrato(5)
print(f"Nome della forma: {quadrato.nome}")
print(f"Area del quadrato: {quadrato.getArea()}")
print("Rendering del quadrato:")
quadrato.render()
