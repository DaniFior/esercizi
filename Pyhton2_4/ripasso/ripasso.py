#avendo una lista di nomi con il voto su dizionari diversi, unire tutto in un dizionario mettendo i voti in una lista unica 

voti: list = [{"nome": "Flavio", "voto":18}, {"nome":"Flavio", "voto":25}]

aggr: dict = {}

aggr: dict = {      #dizionari annidati
    "key_1": {
        "key_1_1": {
                "floor":0
        },
        "key_2_2": {
            "floor":2
        }
    }
}

#DIFFERENZA DUPLA, LISTA: 

a:list = [1,2]
b : tuple = (1,2)

a[0] = 3        #modifica consentita
b[0] = 3        #mi da errore, LE DUPLE NON SONO  MODIFICABILI

i, j = b        #è possibile anche spacchettarle, il valore 1 andrà su i, il valore 2 andrà su j

#scorrere il dizionario annidato
aggr["key_1"]["key_1_1"]["floor"]


for dizionario in voti:

    nome: str = dizionario["nome"]

    voto: str = dizionario["voto"]

    if nome in aggr: 

        aggr[nome].append(voto)

    else:

        aggr[nome] = [voto]

#scorrere i dizionari

for key, value in aggr.items():

    print(key, value)