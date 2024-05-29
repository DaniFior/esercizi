#ESERCIZIO 9-1 e ESERCIZIO 9-4
'''
class Restaurant:
    def __init__(self, name, cusinine_type, number_served = 0) -> None:
        self.name = name
        self.cuisine_type = cusinine_type
        self.number_served = number_served
        
    def set_number_served(self) -> int:
        self.number_served = 15

    def get_number_served(self)-> int:
        return self.number_served

    def describe_restaurant(self) -> str:
            print(f"Name: {self.name}, cuisine type: {self.cuisine_type}, client served: {self.number_served}")
        
    def open_restaurant(self) -> str:
            print("The restaurant is open!")
    
    def set_number_served(self) -> int:
          self.number_served = 15

restaurant : Restaurant = Restaurant("Piramide d'Egitto", "Pizza")   
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant : Restaurant = Restaurant("Piramide d'Egitto", "Pizza", 10)   
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''
#ISTANZE ESERCIZIO 9-4
'''
restaurant.set_number_served()
restaurant.get_number_served()
restaurant.describe_restaurant()

print()
'''
#ESERCIZIO 9-2
'''
restaurant1 : Restaurant = Restaurant("Luvumbo", "Sarda")   
restaurant2 : Restaurant = Restaurant("Giorgetto", "Italiana")   
restaurant3 : Restaurant = Restaurant("Habib", "Araba")   

restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()
print()
'''
#ESERCIZIO 9-3 e ESERCIZIO 9-5
'''
class User:
    def __init__(self, first_name, last_name, email, telephone, login_attempts = 0) -> None:
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
            self.telephone = telephone
            self.login_attempts = login_attempts

    def increment_login_attempts(self) -> int:
        self.login_attempts += 1
    def reset_login_attempts(self) -> int:
        self.login_attempts = 0

    def describe_user(self) -> str:
        print(f"first name: {self.first_name}, last name: {self.last_name}, email: {self.email}, telephone: {self.telephone}, login attempts: {self.login_attempts}")

    def greet_user(self) -> str:
        if self.first_name=="Daniele":
            print("Daniele you are good!")
        elif self.first_name=="Giacomo":
            print("Giacomo is baaaack!")
'''
#ISTANZE ESERCIZIO 9-5
'''
user4 : User = User("Daniele", "Fioravanti", "daniele@gmail.com", "3334532109")
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.describe_user()
user4.reset_login_attempts()
user4.describe_user()
'''
#ISTANZE ESERCIZIO 9-3
'''
user1 : User = User("Daniele", "Fioravanti", "daniele@gmail.com", "3334532109")
user2 : User = User("Marco", "Calafiori", "marco@gmail.com", "3210983245")
user3 : User = User("Giacomo", "Marcantonio", "giacomo@gmail.com", "3658743614")
user1.describe_user()
user2.describe_user()
user3.describe_user()
user1.greet_user()
user2.greet_user()
user3.greet_user()
'''
#ESERCIZIO 9-6
'''
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, number_served = 0, flavours = []) -> None:
        super().__init__(name, cuisine_type, number_served)
        self.flavours = flavours
    
    def get_flavours(self) -> str:
        for i in self.flavours:
             print(i)
    
    def set_flavours(self, flavours) -> str:
        self.flavours = flavours

gelateria : IceCreamStand = IceCreamStand("Gelateria", "Gelato")
gelateria.set_flavours(["crema", "pistacchio", "nocciola"])
gelateria.get_flavours()
'''
#ESERCIZIO 9-7 e 9-8
'''
class User:
    def __init__(self, first_name, last_name, email, telephone, login_attempts=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone
        self.login_attempts = login_attempts

class Admin(User):
    def __init__(self, first_name, last_name, email, telephone, privileges=None, login_attempts=0) -> None:
        super().__init__(first_name, last_name, email, telephone, login_attempts)
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def get_privileges(self):
        return self.privileges

    def set_privileges(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


admin = Admin("Daniele", "Fioravanti", "daniele@gmail.com", "3334758612")
admin.set_privileges(["can add post", "can remove post"])
admin.show_privileges()

class Privileges:
    def __init__(self, privileges=None) -> None:
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def get_privileges(self):
        return self.privileges

    def set_privileges(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin2(User):
    def __init__(self, first_name, last_name, email, telephone, privileges=None, login_attempts=0) -> None:
        super().__init__(first_name, last_name, email, telephone, login_attempts)
        if privileges is None:
            privileges = []
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        self.privileges.show_privileges()

admin2 = Admin2("Daniele", "Fioravanti", "daniele@gmail.com", "3334758612", ["can add post", "can remove post"])
admin2.show_privileges()

privileges = Privileges(["can add post", "can remove post"])
privileges.show_privileges()
'''
#ESERCIZIO 9-9
'''
class Battery:
    def __init__(self, batterysize:int) -> None:
        self.batterysize = batterysize
        self.batterysize = 65

    def upgrade_battery(self):
        if self.batterysize < 65:
            self.batterysize = 65
            print("Battery capacity set to 65")
        elif self.batterysize >= 65:
            return self.batterysize

    def get_range(self):
        #get_range non è una funzione che è stata specificata nel programma
'''
#ESERCIZIO 9-10
'''
from restaurant import Restaurant
restaurant : Restaurant = Restaurant("Piramide d'Egitto", "Pizza")   
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant : Restaurant = Restaurant("Piramide d'Egitto", "Pizza", 10)   
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''
#ESERICIZIO 9-11
'''
from esercizio9_11 import Admin2, Privileges, User
admin2 = Admin2("Daniele", "Fioravanti", "daniele@gmail.com", "3334758612", ["can add post", "can remove post"])
admin2.show_privileges()

privileges = Privileges(["can add post", "can remove post"])
privileges.show_privileges()
'''
#ESERICIZIO 9-13
'''
import random
class Die:
    def __init__(self, sides:int) -> None:
        self.sides = sides

    def roll_die(self):
        numero = random.randint(1,self.sides)
        print(numero) 

class Die2:
    def __init__(self, sides:int) -> None:
        self.sides = sides

    def roll_die(self):
        numero = random.randint(1,self.sides)
        print(numero) 

die : Die = Die(sides=7)

die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()

die : Die = Die(sides=11)
die2 : Die2 = Die2(sides=21)

die.roll_die()
die2.roll_die()
die.roll_die()
die2.roll_die()
die.roll_die()
die2.roll_die()
die.roll_die()
die2.roll_die()
die.roll_die()
die2.roll_die()
'''
#ESERCIZO 9-14
'''
import random
lista = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
my_ticket = ['c', 4, 7, 3]
str = ''
indovinate = 0
ciclo = 0

#superenalotto = random.sample(lista,4)
#print(f"Any ticket matching these: {superenalotto} wins a prize.")

while indovinate <= 4:
    superenalotto = random.sample(lista,4)
    for i in superenalotto:
        ciclo += 1
        if i in my_ticket:
            indovinate += 1
            continue
        else: 
            break

print(f"Sono state necessari {ciclo} cicli.")
'''