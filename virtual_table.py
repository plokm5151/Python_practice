class Shape:
    def draw(self):
        print('Drawing some thing')

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

circle = Circle()
circle.draw()

square=Square()
square.draw()