#Parent Class/Super Class/Base Class

class Animal:
    isMammal = True

    def speak (self):
        print("Animal is speaking")

#Child Class/Sub Class/Derived Class
class Cat(Animal):
    def meow(self):
        print("Cat is Meowing")

    def climbing(self):
        print("Cat is climbing a tree")

class Donkey(Animal):
    hasTail = True

    def move(self):
        print("Donkey is moving")


a = Animal()

c = Cat()

d = Donkey()