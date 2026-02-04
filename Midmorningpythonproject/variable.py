# Variable is a container used to store a value
from time import process_time

school = "eMobilis"
firstname = "John"
lastname = "Smith"
num1 = 45
num2 = 100
language = "Python"
age = 18 #integer
length = 45.6 #float
greeting = "Hello there" #string
hasfeathers = True #Boolen

#Data Structures- Multiple values stored
#one variable

fruits = ["Banana", "Mango", "Pineapple"] # List - Ordered and Changeable - diffrent datatypes
courses = ["MIT", "Data Science", "Cyber Security"] #Array - similar datatypes
cars = ("Mercedes", "Ford", "Nissan", "Toyota" )  #Tuple - Ordered and Unchangeable
countries = {"Kenya", "Mali", "Morocco", "South Africa"} #Set - Unordered and Unchangeable
student = {
    "firstname" : "Esther",
    "course" : "MIT",
    "age" : 19,
    "nationality" : "Kenya",
    "gender" : "Female"

} #Dictionary - Key value pair

print(age)
print("The length is", length)
print(fruits)
print(countries)
print(student["nationality"])

#Typecasting - Coverting one data to another
print(float(age))
print(int(length))









print(school)
print(firstname)
print(lastname)
print(firstname, lastname)
print(school, "is a coding school")
print(language, "python is a web programming language")
print(num1+num2)


print("the sum of", num1,"and", num2, "is", num1+num2 )