#esercizio 4-1
pizzas : list = ["Margherita", "Capricciosa", "Boscaiola"]

for a in pizzas:
    print("\nI like {}".format(a))

#esercizio 4-2

animals : list = ["Cetacea", "Artiodactyla", "Sirenia"]

for a in animals:
    print("\nThis animal is a mammal: {}".format(a))
    if a == "Cetacea":
        print("Cetacea are big")
    elif a == "Artiodactyla" :
        print("Artiodactyla are enourmus")
    else: print("Sirenia are whale")

#esercizio 4-3

for a in range(21):
    print(a, end = " ")
print("\n")

#esercizio 4-4

#yes = input("\nDo you want to print one milion numbers? (Y/N)")
#yes = yes.upper()
#if yes == "Y":
    
    #number: list = []
    #for x in range(1, 1000001):
    #    number.append(x)
    #for x in number:
    #    print(x, end = " ")

#esercizio 4-5

number : list = []
for x in range (1,1000001):
    number.append(x)
print("The smallest number is: \t{}".format(min(number)))
print("\n")
print("The biggest numer is: \t{}".format(max(number)))
print("\n")
print("The summary of 1 million number is: \t{}".format(sum(number)))
print("\n")

#esercizio 4-6

number2 : list = [] 
for x in range (1, 21, 2):
    number2.append(x)
    print(number2)
print("\n")

#esercizio 4-7

three : list = []
for x in range (3, 31, 3):
    three.append(x)
    print(three)
print("\n")

#esercizio 4-8

for x in range (1,11):
    risultato = x ** 3
    print(risultato)
print("\n")

#esercizio 4-9

cubo = list = []
for x in range (1,11): 
    risultato = x ** 3
    cubo.append(risultato)
print(cubo)
print("\n")

#esercizio 4-10

slice : int = 3
print("The first three values in this list are: {}".format(cubo[:slice]))

print("Three values in the middle of the list are: {}".format(cubo[2:5]))
slice2 : int = -3
print("The last three values in this list are: {}".format(cubo[slice2:]))
print("\n")

#esercizio 4-11 

friend_pizzas : list = ["Margherita", "Capricciosa", "Boscaiola"]

friend_pizzas.append("Primavera")
pizzas.append("Marinara")

for pizza1 in friend_pizzas:
    print(f"My friend's favourite pizzas are: {pizza1}")
print("\n")

for pizza2 in pizzas :
    print("My favourite pizzas are: {}".format(pizza2))

