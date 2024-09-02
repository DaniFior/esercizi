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
        if len(self.students) < self.limit:
            self.students.append(student)

    def add_lecturer(self, lecturers):
        if len(self.lecturers) <= self.get_limit_lecturers():
            self.lecturers.append(lecturers)