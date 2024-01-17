from Point import Point
from Line import Line
import math

class Circle():
    def __init__(self, mid: Point, radius: float = None):
        self.mid = mid
        self.radius = radius

    def get_radius(self, point: Point):
        if self.radius:
            return self.radius
        rad_line = Line(self.mid, point)
        r = rad_line.distance
        self.radius = r
        return self.radius
    
    def get_area(self):
        return math.pi * (self.radius ** 2)
    
    def get_circumfrence(self):
        return 2* math.pi * self.radius
    

    
mid = Point(1, -1)
a = Circle(mid)
point = Point(3, 3)
r = a.get_radius(point)
print(r)
print(a.get_area())