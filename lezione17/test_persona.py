#DA RISOLVERE ALCUNI TEST CASE
#DA RISOLVERE ALCUNI TEST CASE
#DA RISOLVERE ALCUNI TEST CASE
#DA RISOLVERE ALCUNI TEST CASE

import unittest 
from dottore import Dottore
from fatture import Fattura
from paziente import Paziente
from persona import Persona

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Mario")
        self.assertEqual(self.persona.getLastname(), "Rossi")
        self.assertEqual(self.persona.getAge(), 0)

    def test_set_name(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.getName(), "Luigi")
        self.persona.setName(123)
        self.assertEqual(self.persona.getName(), "Luigi")

    def test_set_last_name(self):
        self.persona.setLastName("Verdi")
        self.assertEqual(self.persona.getLastname(), "Verdi")
        self.persona.setName(456)
        self.assertEqual(self.persona.getLastname(), "Verdi")

    def test_set_age(self):
        self.persona.setAge(43)
        self.assertEqual(self.persona.getAge(), 43)
        self.persona.setAge("Mario")
        self.assertEqual(self.persona.getAge(), 43)
    
class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", "Ginecologia", 14.3)
    
    def test_initialization(self):
        self.assertEqual(self.dottore.getName, "Mario")
        self.assertEqual(self.dottore.getLastname, "Rossi")
        self.assertEqual(self.dottore.getSpecialization, "Ginecologia")
        self.assertEqual(self.dottore.getParcel, 14.3)

    def test_isValidDoctor(self):
        self.dottore.setAge(35)
        self.assertTrue(self.dottore.isAValidDoctor())
        self.dottore.setAge(25)
        self.assertTrue(self.dottore.isAValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self) -> None:
        self.paziente = Paziente("Luigi", "Mossa", "DHK")
    
    def test_initialization(self):
        self.assertEqual(self.paziente.getName, "Luigi")
        self.assertEqual(self.paziente.getLastname, "Mossa")
        self.assertEqual(self.paziente.getIdCode, "DHK")

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.doctor = Dottore("Giovanni", "Rossi", "Generale", 150.0)
        self.doctor.setAge(40)
        self.paziente1 = Paziente("Andrea", "Neri", "111")
        self.paziente2 = Paziente("Giulia", "Corradi", "222")
        self.patients = [self.paziente1, self.paziente2]
        self.fattura = Fattura(self.patients, self.doctor)

    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary, 300.0)

    def test_add_patient(self):
        new_pazient = Paziente("Luca", "Gialli", "333")
        self.fattura.addPatient(new_pazient) 
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 450.0)
    
    def test_remove_patient(self):
        self.fattura.removePatient("111")
        self.assertEqual(self.fattura.getFatture(), 1)
        self.assertEqual(self.fattura.getSalary(), 150.0)

if __name__ == "__main__":
    unittest.main()
