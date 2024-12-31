class Employee():
    companyname = "Apple"
    area = "india"
    def show(self):
        print(f"The company name is {self.companyname}  & name = {self.name} is from {self.area}")
    
    def changeCompany(cls, newCompany):
        cls.companyname = newCompany
        
    @classmethod        
    def Area(cls, Newarea):
        cls.area = Newarea
        
a = Employee()    
a.name ="Arman"  
a.show()
a.changeCompany("Tesla")
a.show() 
print(Employee.area)
print(Employee.companyname) #the company name will not be changed 

print('\n')

b = Employee()    
b.name ="harry"  
b.show()
b.changeCompany("Tesla")
b.show() 
print(Employee.area)
b.Area("usa") #the area name will  be changed bcause of the @classmethod
b.show() 
print(Employee.area)#the area name will  be changed bcause of the @classmethod




