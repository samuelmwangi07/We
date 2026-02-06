#Functions/Methods - A block of code used to perform a task

# 1. Standard-library/Inbuilt functions - al
y = max(56, 67, 345, 213, 5666, 6788, 2344)
print(y)

x = min(56, 67, 345, 213)
print(x)

# 2. User-Defined Functions
def school():
    print("emobilis")
school() #Calling a function


#Parameters/Variables
#Arguments/Values

def multiply(x, y):
     print(x * y)
multiply(34, 90)
multiply(94, 30)
multiply(84, 20)
multiply(64, 10)

def student(name, age, gender):
    print(name, age, gender)
student("samuel", 18, "Male")
student("James", 19, "Male")


#Python programme to display details of 5 employees at emobilis
#Use a user defined function with the help of parameters and arguments

#Full names ,Position , Age , Gender

def employees(name, position, age, gender):
    print(name, position, age, gender)
employees("Ken Mwenda","Managing Director",57, "Male")
employees("Caroline Ngumbi","Finance Management leader",47, "Female")
employees("Ruth Amoit","Head of Programs",59, "Female")
employees("Kimanzi Mwendwa ","Centre Manager",48, "Male")
employees("Nelson Oginga","ICT Manager",39, "Male")






















