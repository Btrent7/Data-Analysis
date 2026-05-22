class Student():
    def __init__(self, name, house): # __init__  = (function inside a Class)
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property #Getter Function
    def house(self):
        return self._house
    
    @house.setter #Setter Function for all variables called ".house"
    def house(self, house):
        if house not in ["House1", "House2", "House3"]:
            raise ValueError("Invalid house")
        self._house = house
    
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house) #Creates an instance (object) of the Class
    
if __name__ == "__main__":
    main()