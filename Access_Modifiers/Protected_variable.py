class person():
    def __init__(self):
        self._name = "Arman" #this are the Protected variable
        self._id = 1         #this are the Protected variable
    
A = person ()       
print(A._name) # this can be access directly
print(A._id)   # this can be access directly