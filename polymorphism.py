 #Polymorphism is many forms a method can have.

class Rectangle:
     def Draw(self):
         print("Drawing a rectangle")

class Rhombus:
    def Draw(self):
        print("Drawing a Rhombus")

class Parallelogram:
    def Draw(self):
        print("Drawing a Parallelogram")

r = Rectangle()
r.Draw()

rh = Rhombus()
rh.Draw()


p = Parallelogram()
p.Draw()