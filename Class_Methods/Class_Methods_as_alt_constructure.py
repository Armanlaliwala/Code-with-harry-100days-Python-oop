class Employee():
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1] ))
        
e1 = Employee("Harry", 20)    
print(e1.name)
print(e1.salary)

string = "jhon-12000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)