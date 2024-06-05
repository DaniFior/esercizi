class Room:
    
    def __init__(self, id, floor, seats):
        self.area=seats*2
        self.id = id
        self.floor = floor
        self.seats = seats
        
    def get_id(self):
        return self.id
        
    def get_floor(self):
        return self.floor
        
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area
        
class Building:
    
    def __init__(self, name, address, floors:tuple):
        rooms = []
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = rooms
        
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return self.rooms
    
    def add_room(self, room : Room):
        if room.floor >= self.floors[0] and room.floor <= self.floors[1]:
            if room not in self.rooms:
                self.rooms.append(room)
            
    def area(self):
        somma=0
        for room in self.rooms:
            somma += room.area
        return somma