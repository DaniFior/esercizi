# Daniele Fioravanti
# 17/04/2024

name: str = "Mario"
message: str = "Hello {} do you want to learn some python together?".format(name)
print (message)

#DA QUI FATTO A CASA

#esercizio 2-3
name : str = "EriC"
print ("Hello {}, can i teach you some python?".format(name))

#esercizio 2-4
print(str.lower(name))
print(str.upper(name))
print(str.title(name))

#esercizio 2-5 e 2-6

author_name : str = "Steve Jobs"
quote : str = "Stay hungry, stay foolish"
output : str = f"Once {author_name} said: \"{quote}\""

print(output)

#esercizio 2-8

filename : str = "python_notes.txt"
nosuffix : str = filename.removesuffix(".txt")
print(nosuffix)

#esercizio 3-1 e 3-2

names = ["Marco", "Giuseppe", "Francesco"]
print(names[0])
print(names[1])
print(names[2])

print("Hello {}, how are you? ".format(names[0]))
print("Hello {}, how are you? ".format(names[1]))
print("Hello {}, how are you? ".format(names[2]))

#esercizio 3-3

brand = ["Honda", "Suzuki", "KTM", "Yamaha"]
print(f"I would like to own a {brand[0]} motorcycle")
print(f"I would like to own a {brand[1]} motorcycle")
print(f"I would like to own a {brand[2]} motorcycle")
print(f"I would like to own a {brand[3]} motorcycle")

#esercizio 3-4 e 3-5

invites = ["Totti", "De Rossi", "Ranieri", "Ancelotti"]
print("Hello {}, how are you? I would like to invite you for a dinner. Let me known".format(invites[0]))
print("Hello {}, how are you? I would like to invite you for a dinner. Let me known".format(invites[1]))
print("Hello {}, how are you? I would like to invite you for a dinner. Let me known".format(invites[2]))
print("Hello {}, how are you? I would like to invite you for a dinner. Let me known".format(invites[3]))
print(f"Mr. {invites[3]} can't be at your dinner.")
invites.remove("Ancelotti")
invites.append("Guardiola")
print("Mr. {} is the new guest for the dinner.".format(invites[3]))

#esercizio 3-6

print("Hi {}, i want to let you know that i just found a bigger table".format(invites[0]))
print("Hi {}, i want to let you know that i just found a bigger table".format(invites[1]))
print("Hi {}, i want to let you know that i just found a bigger table".format(invites[2]))
print("Hi {}, i want to let you know that i just found a bigger table".format(invites[3]))

invites.insert(0, "Montella")
invites.insert(2, "Pizzarro")
invites.append("Rudiger")
print(f"The new list of the invites is: {invites}")

print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[0]))
print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[1]))
print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[2]))
print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[3]))
print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[4]))
print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[5]))
print("Hi {} there is a new dinner. In my home at 20:30.".format(invites[6]))

#esercizio 3-7

print(invites)
print("Hi everyone, I am sorry but i can invite only 2 guests. ")
print(f"Hi,{invites.pop(6)} but i can't invite you anymore")
print(f"Hi,{invites.pop(5)} but i can't invite you anymore")
print(f"Hi,{invites.pop(4)} but i can't invite you anymore")
print(f"Hi,{invites.pop(3)} but i can't invite you anymore")
print(f"Hi,{invites.pop(2)} but i can't invite you anymore")

print(invites)

del invites[1]
del invites[0]
print (invites)

#esercizio 3-8

cities = ["Rome", "Paris", "Melbourne", "London", "New York"]
print("The original list is: {}".format(cities))
print("The list in alphabetic order is: {}".format(sorted(cities)))
print("The list is still in the original version: {}".format(cities))

#cities.sort(reverse=True)
#print("The list in analphabetic order is: {}".format(cities))
print(sorted(cities, reverse =True ))
print(cities)
#cities = sorted(cities)
#print(cities)

cities.reverse()
print(f"The analphabetic order with the reverse method is: {cities}")

cities.reverse()
print(f"The original version using the reverse method: {cities}")

cities.sort()
print("The list in alphabetic order using the sort method() is: {}".format(cities))

cities.sort(reverse = True)
print("The list in alphabetical order revers using the sort methos() is: {}".format(cities))

print("The original list is changed in: {}".format(cities))

#esercizio 3-9

x = len(invites)
print("The invites for the dinner are: {}".format(x))

#esercizio 3-10

things = ["Everest", "Tevere", "Arno", "Tulipani", "Roma"]
things.append("Ciclamino")
things.remove("Tevere")
things.pop(0)
print("Prova prime modifiche: {}".format(things))
things.insert(2, "Mario")

things.sort()
print(f"Things in alphabetic order {things}")

things.reverse()
print(f"Things in alphabetic inverse order: {things}")



#FINE ESERCIZI 2. e 3.