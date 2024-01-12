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

    def midpoint_to_point(self, midpoint):
        """Returns another point given staring point and midpoint"""
        return Point((midpoint.x*2-self.x), (midpoint.y*2-self.y))



A = Point(1/2, -1)
B = Point(1, -3/4)

#print((A.distance(B)))


M = A.midpoint(B)

#print(M.x, M.y)

M = Point(5, -4)
B = Point(7, -2)

A = B.midpoint_to_point(M)

#print(A.x, A.y)
