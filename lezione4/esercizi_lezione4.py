#esercizio 8-1
"""
def display_message() -> str:
    print("I am learning to code in python")

display_message()
"""
#esercizio 8-2
"""
def favourite_book(title : str = "Alice in wonderland") -> str :
    print(f"My favourite book is {title}")
    return title
title = "Alice in wonderland"
favourite_book(title)
"""
#esercizio 8-3
"""
def make_shirt() -> str :
    size : str = input("Insert your size: ")
    text : str 
    size_maiusc = str.upper(size) 
    
    if size_maiusc == "M" or size_maiusc == "S" or size_maiusc == "L" or size_maiusc == "XL" :
        text = input("Insert the text now: ")
        print("Your order is for a t-shirt size {} \n and your text on it is: {}".format(size_maiusc, text))
    else : 
        print("Size not valid")
    return f"{size_maiusc}, {text}"

make_shirt()
"""
#esercizio 8-4
"""
def make_shirt2(size2 = "L", text2 = "I love python") -> str:
    print (f"The size of the T-shirt is {size2} and the text is: {text2}")

make_shirt2()
make_shirt2(size2 = "M")
make_shirt2(size2= "XL", text2 = "I hate python")
"""
#esercizio 8-5
"""
def describe_city(city : str, country : str = "Italy") -> str :
    print(f"{city} is in {country}")
    return f'{city}{country}'

describe_city(city = "Rome")
describe_city(city = "Venice")
describe_city(city = "Sofia", country="Bulgaria")
"""
#esercizio 8-6
"""
def city_country(name : str, country: str) -> str : 
    print(f"{name},{country}")
    return f'{name},{country}'

city_country(name="Rome", country="Italy")
city_country(name="Sofia", country="Bulgaria")
city_country(name="Amsterdam", country="Netherlands") 
"""
#esercizio 8-7

def make_album(artist : str , title : str) -> str:
    album : dict = {"Title:" : title, "Artist" : artist}
    print(album)
    return make_album

def make_album2(artist : str , title : str, nsong : int = None) -> str:
    album : dict = {"Title:" : title, "Artist" : artist, "Track number: " : nsong}
    print(album)
    return make_album2
"""
make_album(artist="Gemitaiz", title="Veleno 6")
make_album(artist="Fedez",title="Bella storia")
make_album(artist="IlTre", title="Cracovia")
make_album2(artist="IlTre", title="Invisibili", nsong=8)
make_album2(artist="Jovanotti", title="faffi", nsong=2)
"""
#esercizio 8-8
"""
user : dict = {}
i : int = 1
while i < 100 :
    make_album(artist=input("Inserisci il nome dell'artista: "), title=input("Inserisci il titolo dell'album: "))
    quit = input("Vuoi continuare? Y/N ")
    quit = quit.upper()
    if quit == "Y":
        continue
    else:
        break
    i+=1
"""
#esercizio 8-9
"""
message : list = ["Daje Roma", "DDR Vanto Nostro", "Lazio ..."]
def show_messages(message : str) -> str:
    for i in message :
        print(i)
show_messages(message)
    return message
"""
#esercizio 8-10

message : list = ["Daje Roma", "DDR Vanto Nostro", "Lazio ..."]

def send_messages(message : str) -> str:
    sent_messages : list = []
    for x in message :
        print(x)
        sent_messages.append(x)
    for y in sent_messages :
        print(f"Copia di: {y}")
    return sent_messages

send_messages(message)

#esercizio 8-11
copy = send_messages(message)
print(copy, '\n', 'Copia: {}'.format(send_messages(message)))