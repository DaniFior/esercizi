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

class Zoo :
    fences : list = []
    zoo_keepers : list = []

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
        def __init__(self, area, temperature, habitat) -> None:
            self.area=area
            self.temperature=temperature
            self.habitat=habitat
            self.animal : list[Animal] = []
        
        def animal_area(self)->float:
            animalarea=0
            for animal in self.animal:
                animalarea+=animal.height*animal.width
            return animalarea
                
        
class Zookeeper:
        def __init__(self, name, surname, id) -> None:
              self.name=name
              self.surname=surname
              self.id=id
        
        def add_animal(animal:Animal, fence:Fence) -> str:
              if fence.animal_area() < fence.area():
                     