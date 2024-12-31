class employee():
    def __init__ (self, name, id):
        self.name = name 
        self.id = id
        
    def shoedetails(self):
        print(f"the name of the employee {self.id} is {self.name}")
    
class Programmer(employee) :
    def Showlanguage(self):
        print("This default language is py")
        print("This is the text fromthe concept of inheritance")
        
class manager(Programmer)        :
    def showM(self):
        print("This is the text fromthe concept of inheritance Manager")
    
E =employee("Arman", 1)        
E.shoedetails()
e2= Programmer("harry", 2)
e2.shoedetails()
e2.Showlanguage()
e3 = manager("Rubby", 3)
e3.shoedetails()
e3.Showlanguage()
e3.showM()
