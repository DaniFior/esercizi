from film import Film

class Azione(Film):
    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.__penale = 3.0
        self.__genere = "Azione"

    def getGenere(self):
        return self.__genere

    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniritardo:int):
        penale = giorniritardo * self.__penale
        return penale


class Commedia(Film):
    def __init__(self, id: int, titolo: str) -> None:
        super().__init__(id, titolo)
        self.__penale = 2.5
        self.__genere = "Commedia"

    def getGenere(self):
        return self.__genere

    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniritardo:int):
        penale = giorniritardo * self.__penale
        return penale

class Drama(Film):
    def __init__(self, id: int, titolo: str, genere: str) -> None:
        super().__init__(id, titolo)
        self.__penale = 2
        self.__genere = "Drama"

    def getGenere(self):
        return self.__genere

    def getPenale(self):
        return self.__penale
    
    def calcolaPenaleRitardo(self, giorniritardo:int):
        penale = giorniritardo * self.__penale
        return penale