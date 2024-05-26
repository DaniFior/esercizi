class Prodotto:
    def __init__(self, nome : str, quantita : int) -> None:
        self.nome = nome
        self.quantita = quantita
    
class Magazzino:
    def __init__(self) -> None:
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto:Prodotto) -> None:
        if prodotto.nome in self.prodotti:
            self.prodotti[prodotto.nome].quantita += prodotto.quantita
        else:
            self.prodotti[prodotto.nome] = prodotto

    def cerca_prodotto(self, nome)-> str:
        if nome in self.prodotti:
            return self.prodotti[nome]
        else:
            return None

    def verifica_disponibilita(self, nome):
        if nome in self.prodotti and self.prodotti[nome].quantita > 0:
            return True
        else:
            return False


magazzino = Magazzino()

prodotto1=Prodotto("Shampoo", 15)
prodotto2=Prodotto("Bagnoschiuma", 20)
prodotto3=Prodotto("Cavo", 0)

magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)



for prodotto in magazzino.prodotti.values():
    print(prodotto.nome)



nome_prodotto = "Shampoo"
prodotto_trovato = magazzino.cerca_prodotto(nome_prodotto)
if prodotto_trovato:
    print("Articolo disponibile")
else:
    print("Non disponibile")



verifica_disponibilita = "Cavo"
disponibilita = magazzino.verifica_disponibilita(verifica_disponibilita)
if disponibilita:
    print("Articolo con quantita sufficienti")
else:
    print("Articolo con quantita insufficienti")