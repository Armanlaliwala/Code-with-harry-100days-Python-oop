
class student():
    def __init__(self, Name, Roll, Std):
        self.name = Name
        self.roll = Roll
        self.std = Std
    def show(self):
        print(f"{self.name} is from {self.std} Standard and his rollno. is {self.roll}")

class sci_student(student):
    def SciStudent(self):
        print("The student is from the science stream")
    
class com_student(student):
    def com_student(self):
        print("The student is from the Commerce stream")
        
class arts_student(student):
    def arts_student(self):
        print("The student is from the Commerce stream")

a = student("Arman", 1, 12)        
a.show()
print("\n")
b = sci_student("Arkan", 11, 11)
b.show()
b.SciStudent()
print("\n")
c = com_student("Arkam", 12, 21)
c.show()
c.com_student()
print("\n")
d = arts_student("Azban", 11, 121)
d.show()
d.arts_student()