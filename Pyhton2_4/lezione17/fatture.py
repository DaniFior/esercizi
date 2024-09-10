from dottore import Dottore
from paziente import Paziente
class Fattura:
    def __init__(self, patient:list, doctor:Dottore) -> None:
        self.patient = patient
        self.doctor = doctor
        self.fatture : int = 0
        self.salary : int = 0
        if doctor.isAValidDoctor() is True:
            self.fatture = len(self.patient)
        else:
            self.patient = [None]
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
    
    def getSalary(self):
        self.salary = self.fatture * self.doctor.getParcel()
        return self.salary

    def getFatture(self):
        self.fatture = len(self.patient)
        return self.fatture
    
    def addPatient(self, newPatient:Paziente):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor} è stato aggiunto il paziente {newPatient.getIdCode()}")

    def removePatient(self, idCode):
        self.patient.remove(idCode)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.doctor} è stato rimosso il paziente {idCode}")
         