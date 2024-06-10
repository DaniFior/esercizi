from film import Film

class Azione(Film):
    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.penale = 3
        self.genere = "Azione"

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, giorniritardo:int):
        penale = giorniritardo * self.penale
        return penale


class Commedia(Film):
    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.penale = 2.50
        self.genere = "Commedia"

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, giorniritardo:int):
        penale = giorniritardo * self.penale
        return penale

class Drama(Film):
    def __init__(self, id: int, titolo: str, genere: str) -> None:
        super().__init__(id, titolo)
        self.penale = 2
        self.genere = "Drama"

    def getGenere(self):
        return self.genere

    def getPenale(self):
        return self.penale
    
    def calcolaPenaleRitardo(self, giorniritardo:int):
        penale = giorniritardo * self.penale
        return penale