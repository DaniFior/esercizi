#esercizio 5-1

"""car = input("What's your car model?")
str.lower(car)
if car == 'mercedes' or car == 'audi' or car == 'volkswagen' or car == 'ford':
    print ("Your car choise is in the list")
elif  car == 'fiat':
    print("Your car is a special car")
else :
    print("Your car choise is not in the list")"""

#esercizio 5-3

"""
alien_color = 'green' and 'red' and 'yellow'
response = input("Which color is the alien?")
str.lower(response)

if response == 'green' or response == 'yellow':
    print("You just earned 5 points")
elif response == 'red':
    print("You just earned 15 points")
else : print("Exit")     
"""


#esercizio 5-4 + parte iniziale es 5-3 version 1
"""
if response == 'green':
    print("You just earned 5 points")
else :
    print("You just earned 10 points")
"""
#esercizio 5-4 version 2
"""
if response == 'green':
    print("You just earned 5 points")
elif response != 'green':
    print("You just earned 10 points")
"""

#esercizio 5-5 

"""
if response == 'green':
    print("You just earned 5 points")
elif response == 'yellow':
    print("You just earned 10 points")
elif response == 'red' :
    print("You just earned 15 points")
else : 
    print("You earned no points")
"""

#esercizio 5-6

"""
age = input("How old are you? ")
age = int(age)

if age < 2 :
    print("You are a baby")
elif age >= 2 and age < 4 :
    print("You are a toddler")
elif age >= 4 and age < 13 :
    print("You are a kid")
elif age >= 13 and age < 20 :
    print("You are a teenager")
elif age >= 20 and age < 65 :
    print("You are an adult")
elif age >= 65 :
    print ("You are an elder")
else :
    print("ERROR")
"""

#esercizio 5-7

"""
fruit = input("What's your favourite fruit?")
favourite_fruits : list = ["apple", "pineapple", "peach"]
str.lower(fruit)

if fruit in favourite_fruits[0] : 
    print("I really like apple it too!")
elif fruit in favourite_fruits[1] : 
    print("I really like pineapple too!")
elif fruit in favourite_fruits[2] : 
    print("I really like peach too!")
else : print("Sorry I don't like it")
"""
#esercizio 5-8
"""
users : list = ["utente1", "utente2", "utente3", "utente4", "admin"]
login = input("Chi sei?")
if login == users[0]:
    print("Ciao utente1, bentornato")
elif login == users[1]:
    print("Ciao utente2, bentornato")
elif login == users[2]:
    print("Ciao utente3, bentornato")
elif login == users[3]:
    print("Ciao utente4, bentornato")
elif login == users[4]:
    password = input("Inserire password ")
    if password == 'ciao':
        print("Bentornato admin")
    elif password != 'ciao':
        print("Password errata!")
else : print("Utente non valido")
"""

#esercizio 5-9 

users2 : list = []
if not users2:
    print("We need to find some users!")

#esercizio 5-10

