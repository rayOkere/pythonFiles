class Student:
    sock = ""
    def __init__(self):
        print("Student class is initiated.")
    def setName(rock,orange):
        #the names rock and orange don't have to be called that, what matters is the order. 1st parameter
        #lets you access any class property (e.g functions and variables) inside of the class it was typed in
        #2nd parameter holds the value of whatever is passed.
        rock.sock = orange
    def getName(t):
        print(t.sock)
objectname = Student()
objectname.setName("Herald")
objectname.getName()
