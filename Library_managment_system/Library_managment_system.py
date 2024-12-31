class library():
    def __init__(self):
       self.book =[]
       
    def add_book(self, book):
        self.book.append(book)
        print(f"'{book}' has been added.")
        
    def display_books(self):    
        # print(f"The name is {self.book} ")
        if self.book:
            print(f"The name is {self.book} ")
        else:
            print("No book present")
            
    def num_of_books(self):
        return len(self.book)
    
    def check(self):
        if (num_of_books == len(self.book)):
            print("All books are present")
        else:
            print(f"num_of_books is not equal to len(self.book)")
            
print("Library_managment_system")            
my_library = library()     
   
my_library.add_book("Book 1")
my_library.add_book("Book 2")
my_library.add_book("Book 3")
my_library.add_book("Book 4")

my_library.display_books()

num_of_books = my_library.num_of_books()
print(f"the no of books present in the library is : {num_of_books}")

my_library.check()


# Simulate a restart by creating a new instance
print("Restarting the program...")
my_library = library()  # Creating a new instance simulates restarting the program

# Display books in the new instance
my_library.display_books()
