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