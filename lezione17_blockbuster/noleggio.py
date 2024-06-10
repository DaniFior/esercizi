from film import Film
from movie_genere import Azione, Commedia, Drama

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
        if film.title in self.film_list:
            self.film_list.remove(film.title)
            if clientID in self.rented_film:
                self.rented_film[clientID].append(film.title)
            else:
                self.rented_film[clientID] = [film.title]
                print(f"Il cliente {clientID} ha noleggiato {film.title}!")
        else:
            print(f"Non è possibile noleggiare il film {film.title}!")

    def giveBack(self, film, clientID, days):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penalty = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penalty} euro!")
        else:
            print(f"Il cliente {clientID} non ha noleggiato il film {film.getTitle()}")
                
    def printMovies(self):
        for i in self.film_list:
            print(f"{i.getTitle()} - {i.getGenere()}")
    
    def printRentMovies(self, clientID):
        if clientID in self.rented_film and self.rented_film[clientID]:
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenere()} -")
            else:
                print(f"Il cliente {clientID} non ha noleggiato alcun film.")
