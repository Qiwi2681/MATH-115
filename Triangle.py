from Point import Point
from Line import Line

class Triangle:
    def __init__(self, A: Point, B: Point, C: Point) -> None:
        self.A = A
        self.B = B
        self.C = C
        self.ab = Line(A, B)
        self.bc = Line(B, C)
        self.ac = Line(A, C)

    def get_area(self) -> int:
        return (self.ab.distance * self.bc.distance) / 2


a = Triangle(Point(-2, 5), Point(1, 3), Point(-1, 0))
#print(a.get_area())