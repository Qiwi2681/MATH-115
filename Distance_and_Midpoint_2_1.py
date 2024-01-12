import math

class Point():
    """Represents a point of (x, y)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #distance formula
    def distance(self, other):
        """Returns the distance between two points"""
        # Get average of x, y values.
        # We dont care which is larger, root of a square is will always be positive.
        x_dist = self.x - other.x
        y_dist = self.y - other.y 

        # Pythagorean theorem: a^2 + b^2 = c^2  | so | x^2 + y^2 = distance^2
        total_dist_squared = x_dist**2 + y_dist**2

        # Pythagorean theorem:  Square root of distance^2 to distance
        total_dist = math.sqrt(total_dist_squared)

        return total_dist

    #midpoint formula
    def midpoint(self, other):
        """Returns the midpoint between two points"""
        # pretty fuckin simple bud
        x_avg = (self.x + other.x)/2
        y_avg = (self.y + other.y)/2

        return Point(x_avg, y_avg)

    def midpoint_to_point(self, midpoint):
        """Returns another point given staring point and midpoint"""
        # (midpoint.x, midpoint.y)*2 - (given.x - given.y) = (target_x, target_y)

        # 2 * midpoint
        midpoint_x_2 = midpoint.x*2
        midpoint_y_2 = midpoint.y*2

        # midpoint - given point
        other_x = midpoint_x_2-self.x
        other_y = midpoint_y_2-self.y

        return Point(other_x, other_y)



A = Point(1/2, -1)
B = Point(1, -3/4)

#print((A.distance(B)))


M = A.midpoint(B)

#print(M.x, M.y)

M = Point(5, -4)
B = Point(7, -2)

A = B.midpoint_to_point(M)

print(A.x, A.y)

print(math.sqrt(1))
