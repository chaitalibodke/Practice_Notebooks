# -----------------------------------------------------
# Define a class and create its object
# -----------------------------------------------------

class Student:
    # Create the atttributes of the class
    def __init__(self, fname, lname, gender, enrno):
        self.fname   = fname
        self.lname   = lname
        self.gender  = gender
        self.enrno   = enrno
    
    def hello(self):
        print("Hello ", self.fname)


s1 = Student("John", "Smith", "M", "E-001")

s1.hello()

print(s1.enrno)




























