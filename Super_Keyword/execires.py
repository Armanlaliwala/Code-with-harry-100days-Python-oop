class employee():
    def __init__(self, Name, Id):
        self.name = Name
        self.id = Id
class programmer(employee):
    def __init__(self, Name, Id, Lang):
        super().__init__(Name, Id)
        self.lang = Lang
        
ep1 = employee("Rohan", 2)        
ep2 = programmer("arman", 5, "py")

print(ep2.name)
print(ep2.id)
print(ep2.lang)