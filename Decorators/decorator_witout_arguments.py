def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("thanks")
    return mfx()


@greet  #this is a method to use how are you function
def hello():
    print("Hello World")    


print("\n")
