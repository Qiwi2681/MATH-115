import math
from Point import Point

class Line:
    def  __init__(self, a:Point, b:Point) -> None:
        self.a = a
        self.b = b
        self.distance = self.get_distance()
        
    #distance formula
    def get_distance(self):
        """Returns the distance between two points"""
        #___ Algebra clarity, ignore ___#
        a = self.a
        b = self.b
        #___ end ___#

        # Get difference of x, y values.
        a_avg = a.x - b.x
        b_avg = a.y - b.y

        # Pythagorean theorem: a^2 + b^2 = c^2
        # Therefore,  a_avg^2 + b_avg^2 = distance^2
        total_dist_squared = a_avg**2 + b_avg**2

        # Pythagorean theorem:  Square root of distance^2 to distance
        distance = math.sqrt(total_dist_squared)

        return distance

    #midpoint formula
    def midpoint(self) -> Point:
        """Returns the middle point between two points"""
        #___ Algebra clarity, ignore ___#
        a = self.a
        b = self.b
        #___ end ___#

        # pretty fuckin simple bud
        a_mid = (a.x + b.x)/2
        b_mid = (a.y + b.y)/2

        midpoint  = Point(a_mid, b_mid)

        return midpoint
    
a  = Point(5, 3)
b = Point(-7, 6)
L = Line(a, b)
M = L.midpoint()
#print(M.x, M.y)
#print(L.distance)