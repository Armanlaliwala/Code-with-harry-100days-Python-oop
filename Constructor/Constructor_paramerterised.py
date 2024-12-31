class person( ):
    def __init__(self, n, o):        
        self.name = n
        self.occ = o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = person("Arman" , "Developer")        
b = person("harry", "Programmer")        
c =person(1,2)
a.info()
b.info()
c.info()