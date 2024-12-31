class math():
    def __init__(self, num):
        self.num = num
        
    def addtonum(self, n):
        self.num = self.num + n
        
    @staticmethod
    def add(x, y):
        return x + y
    
A =math(5)  
print(A.num)

A.addtonum(6)
print(A.num)

    
# a = math.add(5, 6)   
# print(a)

# def sub(a,b):
#     return a-b
# B = sub(10,5)
# print(B)