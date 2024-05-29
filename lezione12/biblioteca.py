class Libro:
    def __init__(self, titolo:str, autore:str) -> None:
        self.titolo =  titolo
        self.autore = autore
        self.stato = False
    
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo = []

    def aggiungi_libro(self, libro : Libro):
        self.catalogo.append(libro)
        return 'Libro aggiunto al catalogo'

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.stato:
                    return 'Libro non disponibile al prestito'
                else:
                    libro.stato = True
                    return 'Libro prestato'
    
    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.stato:
                    libro.stato = False
                    return 'Libro riconsegnato'
                else:
                    return 'Non possibile riconsegnarlo'

    def mostra_libri_disponbili(self):
        libro_disponibile = [libro.titolo for libro in self.catalogo if not libro.stato]
        if libro_disponibile:
            return f'Libri disponibili: {libro_disponibile}'
        else:
            return 'Non ci sono libri disponibili' 
            

libro1 : Libro = Libro('Harry Potter', 'Rowling')
libro2 : Libro = Libro('Signore degli anelli', 'Totti')
libro3 : Libro = Libro('Se questo è un uomo', 'Primo Levi')

biblioteca : Biblioteca = Biblioteca()


print(biblioteca.aggiungi_libro(libro1))
print(biblioteca.aggiungi_libro(libro2))
print(biblioteca.aggiungi_libro(libro3))

print(biblioteca.presta_libro('Harry Potter'))
print(biblioteca.presta_libro('Signore degli anelli'))

print(biblioteca.restituisci_libro('Harry Potter'))

print(biblioteca.mostra_libri_disponbili())