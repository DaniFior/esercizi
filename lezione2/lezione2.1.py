#ESERCIZIO 6-1 .. 6-12

#esercizio 6-1

#leonardo : dict = {"first_name" : "Leonardo", "last_name" : "Marianella", "age" : 20, "city" : "Rome"}
#print(leonardo["first_name"], leonardo["last_name"], leonardo["age"], leonardo["city"])

#esercizio 6-2 

numbers = {"Valerio" : 10, "Leonardo" : 5, "Daniele" : 69, "Edoardo" : 7, "Mario" : 9}

for numero, persona in numbers.items():
    print("Il numero preferito di {} è: {}".format(persona, numero ))

#esercizio 6-3

glossary : dict = {"print" : "Stampa", "if" : "Loop condizione singola", "Remove" : "Toglie il valore e non lo restituisce"}

for word, significato in glossary.items():
    print("Il significato di {} è:\t {}".format(word, significato))

#esercizio 6-7

leonardo : dict = {"first_name_l" : "Leonardo", "last_name_l" : "Marianella", "age_l" : 20, "city_l" : "Rome"}
valerio : dict = {"first_name_v" : "Valerio", "last_name_v" : "Valerio", "age_v" : 20, "city_v" : "Rome"}
daniele: dict = {"first_name_d" : "Daniele", "last_name_d" : "Fioravanti", "age_d" : 20, "city_d" : "Rome"}

people : list = [leonardo, valerio, daniele]

for dizionario in people: 
    print("\n")
    for k, v in dizionario.items():
        print(f"{k} {v}")

#esercizio 6-8 

cane : dict = {"Tipo" : "Cane", "Razza" : "Labrador", "Owner" : "Daniele"}
gatto : dict = {"Tipo" : "Gatto", "Razza" : "Yoghi", "Owner" : "Leonardo"}
uccello : dict = {"Tipo" : "Uccello", "Razza" : "Aquila", "Owner" : "Valerio"}

pets : list = [cane, gatto, uccello]

for animali in pets:
    print("\n")
    for x, y in animali.items():
        print(f"{x}, {y}")

#esercizio 6-9  
favorite_places : dict = {"Leonardo" : ["Venezia", "Dublino", "Milano"], "Daniele" : ["Amsterdam", "Valencia", "Barcellona"], "Valerio" : ["Melbourne", "Londra", "Verona"]}

for l,m in favorite_places.items():
    print("\nLe città preferite di {} sono: ".format(l))
    for element in m:
        print("\t{}".format(element))

#esercizio 6-10

numbers = {"Valerio" : [10, 7, 8], "Leonardo" : [11, 14, 18], "Daniele" : [69, 71, 98]}

for a,b in numbers.items():
    print ("\nA {} piacciono i numeri: ".format(a))
    for element2 in b:
            print ("\t{}".format(element2))

#esercizio 6-11 

rome : dict = {"Coutry: " : "Italy", "Population: " : 6000000, "Fact: " : "Best city in the world"}
milan : dict = {"Coutry: " : "Italy", "Population: " : 3000000, "Fact: " : "Best underground in the country"}
venice : dict = {"Coutry: " : "Italy", "Population: " : 250000, "Fact: " : "The city with most river in the world"}
cities : dict = {"Rome" : rome, "Milan" : milan, "Venice" : venice}

for c,d in cities.items():
    print("\n{}".format(c))
    for e,f in d.items():
        print (f"{e} {f}")