#create multiple objects
#craete  at least three student objects from the same class with diff values
#and display the same info

#Create a ass called studeclnt
#with the following att: fullname course,age ,feespaid

class Student:
    def __init__(self, fullname, course, age, fees_paid):
        self.fullname = fullname
        self.course = course
        self.age = age
        self.fees_paid = fees_paid

    def info(self):
        print("Full Name:", self.fullname)
        print("Course:", self.course)
        print("Age:", self.age)
        print("Fees Paid:", self.fees_paid)




student1 = Student("Alice Johnson", "Computer Science", 20, 15000)
student2 = Student("Brian Smith", "BBIT", 22, 18000)
student3 = Student("Cynthia Lee", "Engineering", 18, 20000)

# Display student information
student1.info()
student2.info()
student3.info()

