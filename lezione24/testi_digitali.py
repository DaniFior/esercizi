class Documento:
    def __init__(self, testo = '') -> None:
        self.testo = testo

    def getText(self):
        return self.testo
    
    def setText(self, testo):
        self.testo = testo
    
    def isInText(self, parola:str):
        if parola in self.testo:
            return True
        else:
            return False
    
class Email(Documento):
    def __init__(self, mittente ='', destinatario = '', titolo = '', testo = '') -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo

    def getMittente(self):
        return self.mittente
    
    def getDestinatario(self):
        return self.destinatario
    
    def getTitolo(self):
        return self.titolo
    
    def setMittente(self, mittente):
        self.mittente = mittente
    
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
    
    def setTitolo(self, titolo):
        self.titolo = titolo
    
    def getText(self):
        return f'Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}'

    def writeToFile(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.getText())

class File(Documento):
    def __init__(self, nomePercorso="") -> None:
        super().__init__()
        
        self.nomePercorso = nomePercorso
    

    def getNomePercorso(self):
        return self.nomePercorso
    
    def setNomePercorso(self, nomePercorso):
        self.nomePercorso = nomePercorso
    
    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as file:
            self.testo = file.read()

    def getText(self):
        return f'Percorso: {self.nomePercorso}\nContenuto: {self.testo}'



email = Email(mittente="alice@example.com", destinatario="bob@example.com", titolo="Incontro", testo="Ciao Bob, possiamo incontrarci domani?")
file = File(nomePercorso="lezione24/document.txt")

print(email.getText())
file.leggiTestoDaFile()
print(file.getText())
email.writeToFile("email1.txt")
print(email.isInText("incontrarci"))
print(file.isInText("percorso"))



import unittest

class TestDocumento(unittest.TestCase):
    def test_getText_setText(self):
        doc = Documento()
        doc.setText("Questo è un test.")
        self.assertEqual(doc.getText(), "Questo è un test.")

    def test_isInText(self):
        doc = Documento("Questo è un test.")
        self.assertTrue(doc.isInText("test"))
        self.assertFalse(doc.isInText("prova"))

class TestEmail(unittest.TestCase):
    def test_getText(self):
        email = Email(mittente="alice@example.com", destinatario="bob@example.com", titolo="Incontro", testo="Ciao Bob, possiamo incontrarci domani?")
        expected = "Da: alice@example.com, A: bob@example.com\nTitolo: Incontro\nMessaggio: Ciao Bob, possiamo incontrarci domani?"
        self.assertEqual(email.getText(), expected)

    def test_writeToFile(self):
        email = Email(mittente="alice@example.com", destinatario="bob@example.com", titolo="Incontro", testo="Ciao Bob, possiamo incontrarci domani?")
        email.writeToFile("email1.txt")
        with open("email1.txt", 'r') as file:
            content = file.read()
        expected = "Da: alice@example.com, A: bob@example.com\nTitolo: Incontro\nMessaggio: Ciao Bob, possiamo incontrarci domani?"
        self.assertEqual(content, expected)

    def test_isInText(self):
        email = Email(mittente="alice@example.com", destinatario="bob@example.com", titolo="Incontro", testo="Ciao Bob, possiamo incontrarci domani?")
        self.assertTrue(email.isInText("incontrarci"))
        self.assertFalse(email.isInText("ciao"))

class TestFile(unittest.TestCase):
    def test_getText(self):
        file = File(nomePercorso="lezione24/document.txt")
        file.leggiTestoDaFile()
        expected = "Percorso: lezione24/document.txt\nContenuto: Questo è il contenuto del file"
        self.assertEqual(file.getText(), expected)

    def test_isInText(self):
        file = File(nomePercorso="lezione24/document.txt")
        file.leggiTestoDaFile()
        self.assertTrue(file.isInText("contenuto"))
        self.assertFalse(file.isInText("percorso"))

if __name__ == '__main__':
    unittest.main()