class Wizard: #Superclass
    def __init__(self, name):
        if not name:
            raise ValueError("Invalid Name")
        self.name = name
    
    def __str__(self):
        return f"Wizard name: {self.name}"


class Student(Wizard): #Subclass
    def __init__(self, name, house):
        super().__init__(name) #Taking __init__ from Superclass 'Wizard'
        self.house = house
        
    def __str__(self):
        return f"Student name: {self.name}"


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name) #Taking __init__ from Superclass 'Wizard'
        self.subject = subject 
        
    def __str__(self):
        return f"Professor name: {self.name}"

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Dark Arts")

print(wizard)
print(student)
print(professor)