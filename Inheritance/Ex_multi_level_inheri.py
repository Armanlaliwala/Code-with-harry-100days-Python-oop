class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def emp_details(self):
        print(f"the name is {self.name}")
        print(f"the age is {self.age}")

class programmer(Employee)        :
    def __init__(self, name,  lang):
        Employee.__init__(self, name, age = 25  )
        self.lang = lang
        
        
    def emp_details(self):
            Employee.emp_details(self)
            print(f"the language is {self.lang}")
            
class manager(programmer):
    def __init__(self, name,  exp):
        programmer.__init__(self, name,  lang = "py" )
        self.exp = exp
    def emp_details(self):
        programmer.emp_details(self)
        print(f"the experience is {self.exp}")
        
m = manager("Arman", 1)
m.emp_details()

    
    
    