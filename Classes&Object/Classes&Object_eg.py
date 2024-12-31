class person():
    name = "Arman"    # this is a Property
    age = "20"          # this is a Property
    address = "Abad"  # this is a Property
    
    
    def info(self): # this is a method
        print(f"{self.name} age is {self.age} and {self.name} is from {self.address}")
        
        
a=person()   # Creating an instance of the class person
print(a.name,a.age,a.address)  # Outputs: arman 20 abad
a.info() #this info is printed from the def func()
    
a.name = "Danish"    #to udate object
a.age = 22           #to udate object 

print(a.name,a.age,a.address)
a.info() #updates name  #this info is printed from the def func()

b = person()
b.name= "nikita"
b.age = 20
b.info()

c=person(    )  #if we don't pass any details then it will take the class details by default
c.info() #output arman ....