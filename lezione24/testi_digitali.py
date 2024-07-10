class Documento:
    def __init__(self) -> None:
        self.testo = ""

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
    def __init__(self, testo) -> None:
        super().__init__()
        self.mittente = ""
        self.destinatario = ""
        self.titolo = ""
        self.setText(testo)

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

#INIZIARE CLASSE FILE