class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show(self):
        print(f"the name is {self.name}")
        print(f"the species is {self.species}")
        
class dog(animal):
    def __init__(self, name,  breed):
        animal.__init__(self, name, species="dog")
        self.breed = breed
        
    def show(self):
        animal.show(self)
        print(f"the breed of the dog is {self.breed}")
        
class pub():
    def __init__(self, name,  color):
        dog.__init__(self, name, breed="pub")
        self.color = color
        
    def show(self):
        dog.show(self)
        print(f"the color of the dog is {self.color}")
        

D = pub("Bui","black")
D.show()

print("\n")
A = dog("Bui","pub")
A.show()

print("\n")
A = animal("Bui","pub")
A.show()
print("\n")



