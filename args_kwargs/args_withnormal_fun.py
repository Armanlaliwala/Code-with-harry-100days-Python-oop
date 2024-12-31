# *args **kwargs are optional
# this is the function with has normal as well as *agrs.
def func(normal, *args):
    print(normal)
    for item in args:
        print(item)
i = ["arman", "danish", "arkan"]    
normal = "\n this is a normal string coming from the function"
func(normal, *i) # this method with the normal and the *args argument 
