class Person: 
    def __init__(self, name:str, surname:str, ssn:str) -> None:
        """
        
        """
        self._name : str = name
        self._surname : str = surname
        self._ssn : str = ssn

    def get_ssn(self)-> str:
        """
        This function returns a person's ssn
        input:none
        return: self._ssn : str, the function returns the person's ssn
        """
        return self._ssn 

    def get_name(self):
        """
        This function returns a person's name
        input: none
        return: self._name : str, the function returns the person's name
        """
        return self._name


    def set_name(self, name: str)-> None:
        """
        This function set the attribute name
        input: name : str, the parameter contains the user's name
        return : None
        """
        raise Exception("You cannot modify the name!")

    def __str__(self) -> str:
        return f"name: {self._name}, surname: {self._surname}, ssn: {self._ssn}"
 

persona1: Person = Person(name="Daniele", surname="Fioravanti", ssn="FRVDNL04D07H501T")
persona2: Person = Person(name="Mario", surname="Draghi", ssn="MRODRG12G03H501U")

queue: list[Person] = [persona1, persona2]

for person in queue:
    print(person.get_ssn())

print(persona1.get_name())
print(persona1.get_ssn())
print(str(persona1))