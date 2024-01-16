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