class Rainbow:
   def shoe(self):
    return "spoon"
   def blue(self):
    print(self.shoe())
# to call a function, you need to write def at the start and include () at the end, unlike a variable where neither are required.
# the "self" parameter allows you to access class attributes such as variables and functions.
# a global variable is a variable created inside a class and is available everywhere in the class..
# a local variable is a variable exclusive to the function it's in.
class CheckEvenOrOdd:
    def evenOrOdd(self):
     try:
    
        userNumber = input("Please enter a number\n")
        if int(userNumber) % 2 == 0:
            return True
        else:
            return False 
     except:
        print("Something has gone wrong")
        return False
     finally:
        print("The program has been executed")
objectName = CheckEvenOrOdd()
print(objectName.evenOrOdd())
colour1 = Rainbow()
colour1.blue()
