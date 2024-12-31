class employee():
    
    def ShowE(self):
        print("This is the employee class")
        
class  programmer(employee):
    def ShowE(self):
        print("this is in the programmer class")
        super().ShowE()
    def ShowP(self):
        print("This is the programmer class")
        super().ShowE()
        
A = programmer()        
A.ShowP()
A.ShowE() #this will run from programmer class because it is mention in the programmer class 
        