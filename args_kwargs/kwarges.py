
# Example of **kwargs
def func(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, values in kwargs.items()    :
        print(f"{key} is a  {values}")
normal = "this is a normal string coming from the function"
i = ["arman", "danish", "arkan"]    
kw = {
    "arman" : "developer",
    "rohan" : "designer",
    "danish": "Marketing",
    "jeel"   : "seo"
}

func(normal, *i, **kw)# this method with the normal ,*args argument & **kwargs.
# **kwags are in form of dictonary