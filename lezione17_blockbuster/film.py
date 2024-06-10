class Film:
    def __init__(self, id: int, title: str) -> None:
        self.__id = id 
        self.__title = title
    
    def setID(self, id):
        if isinstance(id, int):
            self.__id = id
    
    def setTitle(self, title):
        if isinstance(title, str):
            self.__title = title
        
    def getID(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def isEqual(self, otherFilm:int):
        if otherFilm == self.__id:
            return True
        else:
            return False