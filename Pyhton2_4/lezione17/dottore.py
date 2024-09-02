from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization:str, parcel:float):
        super().__init__(first_name, last_name)

        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            self.specialization = None
            print("La specializzazione inserita non è una stringa!")

        if isinstance(parcel, float):
            self.parcel = parcel
        else:
            self.parcel = None
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self):
        if self.age >= 30:
            print(f" Doctor {self.first_name} {self.last_name} is valid!")
        else:
            print(f" Doctor {self.first_name} {self.last_name} is not valid!")

    def doctorGreet(self):
        Persona.greet()
        print(f"Sono un medico {self.specialization}")
