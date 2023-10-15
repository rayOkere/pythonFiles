class School:
    schoolName = ""
    def __init__(self):
        print("School class is initiated")
    def setSchoolName(self):
        self.schoolName = input("Please enter the name of the school you attend\n")
    def getSchoolName(self):
        return self.schoolName

class Student:
    name = ""
    year = ""
    def __init__(self):
        print("Student class is initiated.")
    def setName(self):
        self.name = input("Please enter your name\n")
    def setYear(self):
        self.year = input("Please enter the year you're in(school)\n")
        #\n at the end of a string makes it appear on a new line
        #the names rock and orange don't have to be called that, what matters is the order. 1st parameter
        #lets you access any class property (e.g functions and variables) inside of the class it was typed in
        #2nd parameter holds the value of whatever is passed.
    def getName(self):
        return self.name
    def getYear(self):
        return self.year
studentObject = Student()
schoolObject = School()
schoolObject.setSchoolName()
studentObject.setName()
studentObject.setYear()
print(schoolObject.getSchoolName())
print(studentObject.getName())

