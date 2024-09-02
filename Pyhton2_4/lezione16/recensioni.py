class Media:
    def __init__(self, title:str) -> None:
        self.title = title
        self.reviews = []

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title
    
    def aggiungiValutazione(self, voto:int):
        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)

    def getMedia(self):
        count = 0
        for i in self.reviews:
            count += i
        media = count / len(self.reviews)
        return media 

    def getRate(self):
        rate = self.getMedia()
        if rate < 1.5:
            return 'Terribile'
        elif rate < 2.5:
            return 'Brutto'
        elif rate < 3.5:
            return 'Normale'
        elif rate < 4.5:
            return 'Bello'
        else:
            return 'Grandioso'
        
    def ratePercentage(self, voto:int):
        count = self.reviews.count(voto)
        percentuale = (count / len(self.reviews)) * 100
        return percentuale
    
    def __str__(self) -> str:
        return f"Film: {self.get_title()}, Valutazione Media: {self.getMedia()}, Giudizio: {self.getRate()}"
    
    def recensione(self):
        print(f'Titolo del Film: {self.get_title()}')

        print(f'Voto medio: {self.getMedia()}')

        print(f'Giudizio: {self.getRate()}')

        print(f'Terribile: {self.ratePercentage(1)}')
        print(f'Brutto: {self.ratePercentage(2)}')
        print(f'Normale: {self.ratePercentage(3)}')
        print(f'Bello: {self.ratePercentage(4)}')
        print(f'Grandioso: {self.ratePercentage(5)}')


class Film(Media):
    def __init__(self, title) -> None:
        super().__init__(title)
    
film1 : Film = Film("Il signore degli anelli")
film2 : Film = Film("Ritorno al futuro")

valutazioni_film1 = [5,5,4,3,5]
for voto in valutazioni_film1:
    film1.aggiungiValutazione(voto)    

valutazioni_film2 = [2,2,3,1,2]
for voto in valutazioni_film2:
    film2.aggiungiValutazione(voto)

film1.recensione()
print("*********************************")
film2.recensione()