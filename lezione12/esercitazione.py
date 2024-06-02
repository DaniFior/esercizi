#ESERCIZIO CONTATORE
'''
class Contatore:
    def __init__(self):
        self.conteggio = 0
    
    def setZero(self):
        self.conteggio = 0
    
    def add1(self):
        self.conteggio += 1
        
    def sub1(self):
        if self.conteggio <= 0:
            print("Non è possibile eseguire la sottrazione")
        else:
            self.conteggio -= 1
    
    def get(self):
        return self.conteggio
        
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")
'''
#ESERCIZIO RICETTA
'''
class RecipeManager:
    def __init__(self):
        self.recipe : dict = {}
        
    def create_recipe(self, name, ingredients:list):
        if name not in self.recipe:
            self.recipe[name] = ingredients
            return self.recipe
        else:
            return "the recipe already exist"
            
    def add_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipe:
            self.recipe[recipe_name].append(ingredient)
            return self.recipe
        else:
            print("la ricetta non esiste o l'ingrediente è già all'interno")
            
    def remove_ingredient(self, recipe_name, ingredient):
        if recipe_name in self.recipe:
            self.recipe[recipe_name].remove(ingredient)
            return self.recipe
        print("la ricetta non esiste o l'ingrediente non è presente")
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name in self.recipe:
            indice = self.recipe[recipe_name].index(old_ingredient)
            self.recipe[recipe_name][indice]=new_ingredient
            return self.recipe
        else:
            return "la ricetta non esiste o l'ingrediente da sostituire non esiste"
    
    def list_recipes(self):
        lista_nome = []
        for x,y in self.recipe.items():
            lista_nome.append(x)
            return lista_nome
            
    def list_ingredients(self, recipe_name):
        if recipe_name in self.recipe:
            return self.recipe[recipe_name]
        else:
            return "la ricetta non esiste"
    
    def search_recipe_by_ingredient(self, ingredient):
        dizionario_mom = {}
        for k,v in self.recipe.items():
            if ingredient in v:
                dizionario_mom[k] = v
        if dizionario_mom:
            return dizionario_mom
        else:
            return "l'ingrediente non si trova in nessuna ricetta"
'''
#ESERCIZIO VEICOLO
'''
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
        
class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
        
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}')
    
class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
        
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}')
'''
#ESERCIZIO ELENTI E BUFFALO -> NON ESCE IL RISULTATO DELLA DENSITA
class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita


    def cresci(self):
        self.popolazione *= (1 + self.tasso_crescita / 100)


    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 1
        popolazione_questa_specie = self.popolazione
        popolazione_altra_specie = altra_specie.popolazione
        
        while popolazione_questa_specie <= popolazione_altra_specie:
            popolazione_questa_specie *= (1 + self.tasso_crescita / 100)
            popolazione_altra_specie *= (1 + altra_specie.tasso_crescita / 100)
            anni += 1
        return anni


    def getDensita(self, area_kmq: float) -> int:
        anni = 1
        popolazione_questa_specie = self.popolazione
        
        while popolazione_questa_specie / area_kmq < 1:
            print(f"Anno {anni}: Popolazione = {popolazione_questa_specie}, Densità = {popolazione_questa_specie / area_kmq}")
            popolazione_questa_specie *= (1 + self.tasso_crescita / 100)
            anni += 1
        
        print(f"Anno {anni}: Popolazione = {popolazione_questa_specie}, Densità = {popolazione_questa_specie / area_kmq}")
        return anni


class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)


class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)