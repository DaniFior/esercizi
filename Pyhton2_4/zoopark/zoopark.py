#PROGETTO ZOOPARK DI DANIELE FIORAVANTI
#CYBER SECURITY

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
        
        def animal_area(self) -> float:
            '''
                This function calcolate the area of animals.
                input: animal height and width
                return: area of the animal
            '''
            animalarea=0
            for animal in self.animal:
                animalarea+=animal.height*animal.width
            return animalarea
        
        def add_animal(self, animal) -> float:
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

        def remove_animal(self, animal) -> float:
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
        
        def feed(self, fence:Fence, animal:Animal) -> float: 
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
    def __init__(self) -> None:
        self.fences = []
        self.zookeepers = []

    def add_fence(self, fence) -> None:
        '''
            This function add the fence to the fence list.
            input: fence
            return: None
        '''
        self.fences.append(fence)

    def add_zookeeper(self, zookeeper) -> None:
        '''
            This function add the zookeeper to the zookeeper list.
            input: zookeeper
            return: None
        '''
        self.zookeepers.append(zookeeper)

    def clean(self) -> float:
        '''
            This function clean the fence.
            It calculate the time that the zookeeper need to clean the fence with a math formule written in the exercise.
            return: time for cleaning the fence
        '''
        total_cleaning_time = 0.0
        for fence in self.fences:
            
            if fence.animal:
                cleaning_time = fence.areafence / (fence.areafence - (fence.areafence - sum(animal.height * animal.width for animal in fence.animal)))
                total_cleaning_time += cleaning_time
            
            else:
                cleaning_time = fence.areafence
                total_cleaning_time += cleaning_time
        
        return total_cleaning_time

    def describe_zoo(self) -> str:
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