class myclass:
    def __init__(self, values):
        self._values = values
    def show(self):
        print(f"the current values is {self._values}")
        
    @property #creating a getter 
    def ten_x_values(self):
        return 10 * self._values
    
    @ten_x_values.setter #creating a setter
    def ten_x_values(self, new_values):
        self._values = new_values/10
            
obj = myclass(10) #sending the values to the method
obj.show() #calling the show method
print(f"the value after 'getter' is {obj.ten_x_values}")  #it will print 100 as 
obj.ten_x_values = 67 #setting the values 
print(f"the  value after setter  is {obj.ten_x_values}") 
obj.show()      