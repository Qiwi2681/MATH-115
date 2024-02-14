from Point import Point


"""
standard form is (x - h)^2/a^2  (y - k)^2/b^2
"""
class Hyperbola:
    def __init__(self, x, y, m: Point):
        self.x = x
        self.y = y
        self.h = m.x
        self.k = m.y
        self.a = None
        self.b = None

    def get_vertex(self):
        x = -self.h
        y = -self.k
        return Point(x, y)

    