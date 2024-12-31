class shape():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class circle(shape):
    def  __init__(self,Rad):
        self.Rad = Rad  
        super().__init__(Rad, Rad)
         
    def area(self):
        return 3.14 * super().area()
    
rec = shape(15, 3)    
print(rec.area())

circ = circle(5)
print(circ.area())