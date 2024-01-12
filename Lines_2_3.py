import math
from Distance_and_Midpoint_2_1 import Point

class Line():
    """"Class representing a line"""
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.slope = self.get_slope()

    def get_slope(self):
        """Get slope of line"""
        # real increase
        rise  = self.end.y - self.start.y
        run = self.end.x - self.end.y

        # average increase or "slope"
        slope = rise/run

        return slope
    

a = Point()