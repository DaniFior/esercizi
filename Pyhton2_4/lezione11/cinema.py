class Film:
    def __init__(self, titolo:str, durata:int) -> None:
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, numero_sala:int, film:Film, posti_totali : int) -> None:
        self.numero_sala = numero_sala
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0

    def prenota_posti(self, num_posti : int) -> str:
        posti_liberi = self.posti_totali - self.posti_prenotati
        if num_posti <= posti_liberi:
            self.posti_prenotati += num_posti
            return f"Posti prenotati {num_posti}"
        else:
            return "Inserisci meno posti, sala piena"

    def posti_disponibili(self) -> str:
        liberi = self.posti_totali - self.posti_prenotati
        print(f"Posti disponibili: {liberi}")

class Cinema:   #gestisce operazioni della sala
    def __init__(self) -> None:
        self.sale = []
    
    def aggiungi_sala(self, sala:Sala):
        self.sale.append(sala)
        print("Sala aggiunta")
    
    def prenota_film(self, titolo_film:str, num_posti:int):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return "Film not found"


cinema = Cinema()
film1 = Film("Interstellar", 120)
sala1  =Sala(1, film1, 100)
cinema.aggiungi_sala(sala1)
print(cinema.prenota_film("Interstellar", 5))
print(cinema.prenota_film("Interstellar", 95))
print(cinema.prenota_film("Interstellar", 1))