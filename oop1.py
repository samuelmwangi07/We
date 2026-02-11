class Dog:

    def __init__(self,name,breed,hasFur):
        self.name = name
        self.breed = breed
        self.hasFur = hasFur
    def bark(self):
        print(self.name"Woof!!")
    def locomotive(self):
        print("Dog is Walking")

dog1 = Dog("Jake","Bulldog","true")
print(dog1.name, dog1.breed, dog1.hasFur)
dog1.bark()

dog2 = Dog("Kala", "Japanese spitz", "true")
print(dog2.name, dog2.breed, dog2.hasFur)
dog2.bark()


dog3 = Dog("Nala","German Shepherd","True")
print(dog3.name, dog3.breed, dog3.hasFur)
dog3.bark()