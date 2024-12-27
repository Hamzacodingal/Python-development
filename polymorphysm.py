class square:
    def __init__(self,side):
        self.side = side
    def area(self):
        print("Area Of The square is",self.side*self.side)

class circle:
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter
    def area(self):
        print("Area Of The circle is",3.14*self.radius*self.radius)
        print("diameter of Circle is, ",self.diameter)
d = square(7)
d.area()
f = circle(7,3.5)
f.area() 