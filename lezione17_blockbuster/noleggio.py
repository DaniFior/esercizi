class Noleggio:
    def __init__(self, film_list : list) -> None: #rented_film: {CHIAVE : INT, LISTA FILM AFFITTATI : LIST}
        self.film_list:list = film_list
        self.rented_film:dict = {}
    
    def isAvaiable(self, film):
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film}")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film}")
            return False
    
    def rentAMovie(self, film, clientID):
        if film in self.film_list:
            self.film_list.remove(film)
            if clientID in self.rented_film:
                self.rented_film[clientID].append(film)
            else:
                self.rented_film[clientID] = [film]
                print(f"Il cliente {clientID} ha noleggiato {film}!")
        else:
            print(f"Non è possibile noleggiare il film {film}!")

    def giveBack(self, film, clientID, days):
        pass
    