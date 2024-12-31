class Example:
    class_variable = 10  # Class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance variable
    
# Usage
instance1 = Example(20)
instance2 = Example(30)

print(Example.class_variable)  # Accessing class variable
print(instance1.instance_variable)  # Accessing instance variable for instance1
print(instance2.instance_variable)  # Accessing instance variable for instance2

