class Film:
    def __init__(self, id: int, titolo: str) -> None:
        self.id = id 
        self.titolo = titolo
    
    def setID(self, id):
        if isinstance(id, int):
            self.id = id
    
    def setTitle(self, title):
        if isinstance(title, str):
            self.title = title
        
    def getID(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def isEqual(self, otherFilm:int):
        if otherFilm == self.id:
            return True
        else:
            return False