# Fence avra self.area, self.temp, self.habitat E SELF.ANIMAL. Scrivere una funziona che calcola l'area occupata: prende lista animali, 
#           la scorre e si salva tutte le area, restituendo il valore disponibile
# Zookeeper avra self.name, self.surname, self.id. ATTENZIONE al fatto che possono pulire i recinti, nutrire animali e altri compiti
# FUNZIONALITA:
# Funzione: 
    # add_animal (va messa nella classe zookeeper), verifica prima disponibilità e verifica se dimensione abbastanza grande per 
    #       contenerlo verificare anche se l'habitat coincide con quello preferito e aggiornare l'area disponibile    
    # feed (va messa nella classe zookeeper), attenzione alla crescita dell'area
    # clean (va messa nella classe zookeeper)
    # describe_zoo (va messa nella classe zoo), devono tornare tutti i valori dei guardini e delle fence

class Animal: 
        def __init__(self, name:str, species:str, age:int, height:int, width:int, preferred_habitat:str, health:float) -> None:
              self.name=name
              self.species=species
              self.age=age
              self.height=height
              self.width=width
              self.preferred_habitat=preferred_habitat
              self.health=health

              self.health = round(100*(1/age), 3)
    
class Fence:
        def __init__(self, areafence, temperature, habitat) -> None:
            self.areafence=areafence
            self.temperature=temperature
            self.habitat=habitat
            self.animal : list[Animal] = []
        
        def animal_area(self)->float:
            '''
                This function calcolate the area of animals.
                input: animal height and width
                return: area of the animal
            '''
            animalarea=0
            for animal in self.animal:
                animalarea+=animal.height*animal.width
            return animalarea
        
        def add_animal(self, animal):
            '''
                This function add animal to fence. 
                First of all calcolate if the fence has enough area for the animal.
                It add the animal inside the fence and update the area of the fence that is now occupated by the animal.
                Input: animal
                return: area fence
            '''
            if self.areafence >= animal.height * animal.width:
                self.animal.append(animal)
                self.areafence -= animal.height * animal.width

        def remove_animal(self, animal):
            '''
                This function remove animal to fence. 
                It add the area that was occupated by the animal that now is free.
                Input: animal
                return: area fence
            '''
            if animal in self.animal:
                self.animal.remove(animal)
                self.areafence += animal.height * animal.width
        
class Zookeeper:
        def __init__(self, name, surname, id) -> None:
              self.name=name
              self.surname=surname
              self.id=id
        
        def feed(self, fence:Fence, animal:Animal):
            '''
                This function feed the animal.
                It calculate if there is enough area for feed the animal,
                then it add 1% of the health and grow up the width and height by 2%.
            '''
            if animal in fence.animal:
                if fence.areafence >= animal.height*animal.width:
                    animal.health += 1
                    animal.width *= 1.02
                    animal.height *= 1.02
            
class Zoo:
    def __init__(self):
        self.fences = []
        self.zookeepers = []

    def add_fence(self, fence):
        '''
            This function add the fence to the fence list.
            input: fence
            return: None
        '''
        self.fences.append(fence)

    def add_zoo_keeper(self, zookeeper):
        '''
            This function add the zookeeper to the zookeeper list.
            input: zookeeper
            return: None
        '''
        self.zookeepers.append(zookeeper)

    def clean(self):
        '''
            This function clean the fence.
            It calculate the time that the zookeeper need to clean the fence with a math formule written in the exercise.
            return: time for cleaning the fence
        '''
        total_cleaning_time = 0.0
        for fence in self.fences:
            
            if fence.animal:
                cleaning_time = fence.areafence / (Fence.areafence - (Fence.areafence - sum(Animal.height * Animal.width for animal in Fence.animal)))
                total_cleaning_time += cleaning_time
            
            else:
                cleaning_time = fence.areafence
                total_cleaning_time += cleaning_time
        
        return total_cleaning_time

    def describe_zoo(self):
        '''
            This function print every information about the zoo.
            Firstly it prints the zookeeper, then the fence and each animal inside this specific fence.

        '''
        
        print("Guardians:")
        for Zookeeper in self.zookeepers:
            print(f"ZooKeeper(name={Zookeeper.name}, surname={Zookeeper.surname}, id={Zookeeper.id})")
        

        print("\nFences:")        
        for fence in self.fences:
            print(f"Fence(area={fence.areafence}, temperature={fence.temperature}, habitat={fence.habitat})")
            print("with animal:")
                        
            for animal in fence.animal:
                print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})")
        
        
        
        print("#" * 30)


#Istanze create con chatgpt 

# Creazione degli animali
lion = Animal("Simba", "Lion", 5, 3, 4, "Savannah", 100)
tiger = Animal("Shere Khan", "Tiger", 6, 3, 3, "Jungle", 100)
elephant = Animal("Dumbo", "Elephant", 8, 6, 7, "Savannah", 100)

# Creazione delle recinzioni
savannah_fence = Fence(100, "Warm", "Savannah")
jungle_fence = Fence(120, "Tropical", "Jungle")

# Creazione degli zookeeper
zookeeper1 = Zookeeper("John", "Doe", 12345)
zookeeper2 = Zookeeper("Daniele", "Daww", 54321)

# Creazione dello zoo
zoo = Zoo()

# Aggiunta delle recinzioni allo zoo
zoo.add_fence(savannah_fence)
zoo.add_fence(jungle_fence)

# Aggiunta degli zookeeper allo zoo
zoo.add_zoo_keeper(zookeeper1)
zoo.add_zoo_keeper(zookeeper2)

# Alimentazione degli animali
zookeeper1.feed(savannah_fence, lion)
zookeeper1.feed(jungle_fence, tiger)
zookeeper2.feed(savannah_fence, elephant)

# Aggiunta degli animali alle recinzioni
savannah_fence.add_animal(lion)
jungle_fence.add_animal(tiger)
savannah_fence.add_animal(elephant)

# Descrizione dello zoo
zoo.describe_zoo()