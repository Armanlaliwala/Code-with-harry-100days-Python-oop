class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def emp_details(self):
        print("This just an employee")

class programmer(Employee)        :
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang
    def emp_details(self):
        print("this is a programmer")
    
class manager(Employee):
    def __init__(self, name, age, exp):
        super().__init__(name, age)
        self.exp = exp
    def emp_details(self):
        print("this is a manager")
        
E = Employee("Arman", 10)        
E.emp_details()
print(f"Name = {E.name}")
print(f"Age is {E.age}")
print("\n")
P = programmer("kai", 12, "Py")        
P.emp_details()
print(f"Name = {P.name}")
print(f"Age is {P.age}")
print(f"Language = {P.lang}")
print("\n")
M = manager("buap", 2, 6)        
M.emp_details()
print(f"Name = {M.name}")
print(f"Age is {M.age}")
print(f"Experiance = {M.exp}")
    
    
    