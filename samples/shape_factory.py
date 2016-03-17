import random
class Shape:
    #create stuff based on class name
    def factory(kind):
        if kind == "Circle":
            return Circle()
        if kind == "Square":
            return Square()
        assert 0, "Bad shape creation: " + kind
    factory = staticmethod(factory)

class Circle(Shape):
    def draw(self):
        print('Circle.draw')
    def erase(self):
        print('Circle.erase')

class Square(Shape):
    def draw(self):
        print('Square.draw')
    def erase(self):
        print('Square.erase')

def shapeNameGen(n):
    kinds = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(kinds).__name__

shapes = [Shape.factory(i) for i in shapeNameGen(5)]

for shape in shapes:
    shape.draw()
    shape.erase()
