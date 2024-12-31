class person():
    def __init__(self):
        self.__name = "Arman" #this are the Private variable
        self.__id = 1         #this are the Private variable
A = person ()       
# print(A.__name) # this cant be access directly
# print(A.__id)   # this cant be access directly

print(A._person__name) # this can be access indirectly
print(A._person__id)   # this can be access indirectly