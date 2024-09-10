#FILE 1

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

#FILE 2

class Person:
    def __init__(self, cf, name, surname, age):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age  

class Student(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group : Group = None
    
    def set_group(self, group):
        self.group = group

class Lecturer(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)

class Group:
    def __init__(self, name, limit) -> None:
        self.name = name
        self.limit = limit
        students=[]
        self.students = students
        lecturers=[]
        self.lecturers = lecturers
        self.limit_lect = 0

    
    def get_name(self):
        return self.name
    
    def get_limit(self):
        return self.limit
    
    def get_students(self):
        return self.students
    
    def get_limit_lecturers(self):
        cont = 0
        for i in self.students:
            cont += 1
            if cont % 10 == 0:
                self.limit_lect += 1
        return int(self.limit_lect)
    
    def add_student(self, student:Student):
        if student not in self.students:
            if len(self.students) < self.limit:
                self.students.append(student)

    def add_lecturer(self, lecturers):
        if len(self.lecturers) <= self.get_limit_lecturers():
            self.lecturers.append(lecturers)

#FILE 3

class Course:
    def __init__(self, name) -> None:
        groups:list = []
        self.groups = groups
        self.name = name
    
    def register(self, student : Student):
        for i in self.groups:
            if len(i.get_students()) < i.get_limit() and student not in i.get_students():
                i.add_student(student)
                return

    def get_groups(self):
        return self.groups
    
    def add_group(self, group:Group):
        self.groups.append(group)