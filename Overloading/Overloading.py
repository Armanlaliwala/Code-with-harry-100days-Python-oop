class vector:
    def __init__(self, i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x ):
        return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k" #this return a string data typr
    
    def __add__(self,x ):
        return vector (self.i + x.i , self.j + x.j , self.k + x.k) #this return a vector data typr
    
v = vector(3,5,4)    
print(v)

v1 = vector(1,2,7)    
print(v1)

print(v + v1)