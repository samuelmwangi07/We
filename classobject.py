 #Class is a blueprint of an object
 #Object is an instance of a class
class Employee:
      #Attributes/Variables
      name = "James"
      age = 45
      gender = "Male"
      salary = 70000.0

      #Behaviour/Function

      def eat(self):
          print("Employee eats")

Employee1 = Employee() #Creating an object
print(Employee1.name)

Employee2 = Employee()
print(Employee2.name)


Employee3 = Employee()