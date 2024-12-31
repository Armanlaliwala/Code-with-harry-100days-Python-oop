class Employee():
    CompanyName = "Apple" #classvariable
    num_employee= 0
    def __init__(self, Name):
        self.name = Name
        self.raise_amount = 0.2
        Employee.num_employee += 1
    def showDetails(self):
        print(f"the name of the employee is {self.name}, is from {self.num_employee} size {self.CompanyName} and the raise in the  amount is {self.raise_amount}")
        
emp1 = Employee("ARman")        
emp1.raise_amount = 0.3
emp1.CompanyName = "ibok"
emp1.showDetails()
        
emp2 = Employee("harr")        
emp2.raise_amount = 0.5
emp2.showDetails()

emp3 = Employee("cao")        

emp3.showDetails()