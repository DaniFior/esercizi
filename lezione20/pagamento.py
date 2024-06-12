class Pagamento:
    def __init__(self, importo) -> None:
        self.setPagamento(importo)
    
    def setPagamento(self, importo):
        self.__importo = importo 
    
    def getPagamento(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: {self.getPagamento()}")
        print("********************")

class PagamentoContanti(Pagamento):
    def __init__(self, importo) -> None:
        super().__init__(importo)
        self.setPagamento(importo)
    
    def dettagliPagamento(self):
        print(f"Pagamento in contanti di: {self.getPagamento():.2f}")

    def inPezziDa(self):
        importo = self.getPagamento()
        banconote = [500, 200, 100, 50, 20, 10, 5]
        monete = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]

        for banconota in banconote:
            num_banconote = int(importo / banconota)
            if num_banconote > 0:
                print(f"{num_banconote} banconota da {banconota} euro")
                importo -= num_banconote * banconota
        for moneta in monete:
            num_monete = int(importo / moneta)
            if num_monete > 0:
                print(f"{num_monete} monete da {moneta} euro")
                importo -= num_monete * moneta
        print("********************")

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo, nometitolare : str, scadenza:str, numerocarta:int) -> None:
        super().__init__(importo)
        self.setPagamento(importo)
        self.nometitolare = nometitolare
        self.scadenza = scadenza
        self.numerocarta = numerocarta

    def dettagliPagamento(self):
        print(f"Pagamento di: {self.getPagamento():.2f} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nometitolare}")
        print(f"Data di scadenza: {self.scadenza}")
        print(f"Numero della carta: {self.numerocarta}")
        print("********************")

pagamento = Pagamento(150.0)
pagamentocontanti = PagamentoContanti(150.0)
pagamentocartacredito = PagamentoCartaDiCredito(150.0, "Daniele Fioravanti", "17/04/2034", 547813459874)

pagamento.dettagliPagamento()
pagamento.getPagamento()
pagamentocontanti.dettagliPagamento()
pagamentocontanti.inPezziDa()
pagamentocartacredito.dettagliPagamento()