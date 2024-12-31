class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"The name of the employye is {self.name} & its id is {self.id}")
class manager(employee):
    def __init__(self, name, id, exp):
        employee.__init__(self, name, id)
        self.exp = exp
    def show(self):
        print(f"The Manager name is {self.name}, manager id is {self.id} & its experiance is {self.exp}")
class programmer(employee):
    def __init__(self, name, id, lang):
        employee.__init__(self, name, id)
        self.lang = lang
    def show(self):
        print(f"The Programmer name is {self.name}, Programmer id is {self.id} & its Language is {self.lang}")

emp1 = programmer("Arman", "7", "py")        
emp1.show()
emp5 = manager("minu", "17", "sales")        
emp5.show()