def my_loop():
    i = 0
    for i in range(500):
        print(i)
        i=  i+1
print("this is the normal loop : ")    
# we are just calling and printing the data, it is stored in the memory    
my_loop()# calling function my_loop
#  this is normal loop

def my_gen():
    i = 0
    for i in range(500):
        yield i        
        i=  i+1
        
print("this is from a generator : ")        
gen = my_gen()   # calling function my_gen
print(next(gen))     
print(next(gen))     
print(next(gen))     

# we are just calling and printing the data, it is not stored in the memory
for j in gen: #this gen will print all the number in the range 
    print(j)    