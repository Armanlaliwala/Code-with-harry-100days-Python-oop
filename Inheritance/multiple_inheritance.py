class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")
        
class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f"The Dance is {self.dance}")
        
class Dancer_Employee( Dancer, Employee): #the class which is call first will be printed.
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
        
    # def show(self): #if we want to print both then we can do this 
    #     Employee.show(self)
    #     Dancer.show(self)

emp1 =Dancer_Employee("kathak", "shivani")        
print(emp1.name)
print(emp1.dance)
emp1.show()
print(Dancer_Employee.mro())
