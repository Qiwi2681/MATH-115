import math

class Point():
    """Represents a point of (x, y)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #distance formula
    def distance(self, other):
        """Returns the distance between two points"""
        return math.sqrt((pow((other.x - self.x), 2) + pow((other.y - self.y), 2)))

    #midpoint formula
    def midpoint(self, other):
        """Returns the midpoint between two points"""
        return Point((self.x + other.x)/2, ((self.y + other.y)/2))

A = Point(3, 5)
B = Point(7, 9)

print((A.distance(B)))


mid = A.midpoint(B)

print(mid.x, mid.y)
