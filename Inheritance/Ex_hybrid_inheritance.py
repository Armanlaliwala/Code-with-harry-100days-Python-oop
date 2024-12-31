class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"the name is {self.name}, and the age is {self.age}")
        
class manager(employee):
    def __init__(self, name, age, exp):
        super().__init__(name, age)
        self.exp = exp

    def show(self):
        print(f"Manager Name: {self.name}, Age: {self.age}, Experience: {self.exp}")

class programmer(employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang
        
    def show(self):
        print(f"Programmer Name: {self.name}, Age: {self.age}, Language: {self.lang}")
        
class teamlead(programmer, manager, employee): #the class which is first will be printed first
    def __init__(self, name, age, exp, lang):
        employee.__init__(self, name, age)        
        self.exp = exp
        self.lang = lang
        
    def show(self): #this will be called , if the is not present then upper part will be called 
        print(f"Team Lead Name: {self.name}, Age: {self.age}, Experience: {self.exp}, Language: {self.lang}")

emp1 = teamlead( "shivani", 29, 6, "py")        
print(emp1.name)
emp1.show()        
        
