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