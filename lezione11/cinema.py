class Film:
    def __init__(self, titolo:str, durata:int) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, id:int, num_posti:int, posti_occ:int,  film : Film = Film()) -> None:
        self.id = id
        self.film = film
        self.num_posti = num_posti
        self.posti_occ = posti_occ

    def prenota_posti(self) -> str:
        richiesta = 0
        if richiesta < self.num_posti and richiesta < self.posti_occ:
            self.posti_occ =- richiesta
            print("Prenotazione effettuata")
        else:
            print("ERROR! Prova ad inserire meno posti, la sala è piena!")
        return self.posti_occ

    def posti_disponibili(self) -> str:
        liberi = self.num_posti - self.posti_occ
        print(f"Posti disponibili: {liberi}")

class Cinema:   #gestisce operazioni della sala
    def __init__(self, sala : list[Sala], elenco_sale : list = [], elenco_film : list = []) -> None:
        self.sala = sala   
        self.elenco_sale = elenco_sale
        self.elenco_film = elenco_film
    
    def aggiungi_sala(self):
        self.elenco_sale.append(self.sala)
        print("Sala aggiunta")
    
    def prenota_film(self, titolo, num_posti, elenco_film) -> str:
        if self.film in elenco_film:
            self.sala.prenota_posti()


film1 : Film = Film("Back to the future", 130)
film2 : Film = Film("Avengers", 340)
film3 : Film = Film("Aldo, Giovanni e Giacomo", 95)

sala1 : Sala = Sala(1, 110, 43, film1)
sala2 : Sala = Sala(2, 90, 13, film3)
sala3 : Sala = Sala(3, 250, 120, film2)
        
cinema1: Cinema = Cinema(sala1, film1 )






