def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("thanks")
    return mfx


print("1) The first time \n")

@greet  #this is a method to use how are you function
def hello():
    print("Hello World") 
hello()

print("\n")

print("2) The second time \n")
greet(hello()) #this is a short cut method to use how are you function

# @greet
def add(a,b):
    print( a+b)
greet(add)(1,5)
print(greet(add)(5,5))