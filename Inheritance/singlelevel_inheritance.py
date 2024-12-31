class animal():
    def __init__(self, name, Age):
        self.name = name
        self.age  = Age
        
    def makesound(self):
        print("This animal make sound")
        print(f"{self.name}, {self.age}")

        
class dog(animal):
    def __init__(self, name, Age, breed):
        super().__init__(name, Age)
        self.breed = breed
        
    def makesound(self):
        print("Baw Baw")
        print(f"{self.name}, {self.age}, {self.breed}")

        
class cat(animal):
    def __init__(self, name, Age, breed):
        super().__init__(name, Age)
        self.breed = breed
        
    def makesound(self):
        print("meow meow")
        print(f"{self.name}, {self.age}, {self.breed}")
        
A = animal("boy", 2)        
A.makesound()

D = dog("doy", 2, "dobberman")        
D.makesound()

C = cat("mo", 3, "persian")   
C.makesound()
