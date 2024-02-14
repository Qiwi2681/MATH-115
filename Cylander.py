from typing import Any
from Point import Point, Point3D
from Circle import Circle
import math
import bisect
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

class Cylander:
    """Class representing a cylander"""
    def __init__(self, circle: Circle, height: int) -> None:
        self.circle = circle
        self.height = height
        self.Volume = self.get_volume()

    def get_volume(self):
        """Returns the volume of the cylander"""
        Circle_Area = self.circle.get_area()
        self.Volume = Circle_Area * self.height

c = Circle(Point(0, 0), radius=1)

cyl = Cylander(c, height=5.000001)

print(cyl.Volume)


#this is 1/3 of a cylander
class Cone():
    def __init__(self, circle, height, vertex) -> None:
        self.circle = circle
        self.circle_area = self.circle.get_area()
        self.vertex = vertex
        self.height = height  # Change to float
        self.volume = self.get_volume()
        self.points = []

    def get_points(self):
        for i in range(0, int(self.height * 10) + 1):  # Convert height to int for the loop
            z = i / 10
            area = self.circle_area * (self.height / 3)
            r = math.sqrt(area / math.pi)

            h, k = self.vertex[0], self.vertex[1]

            for angle in range(0, 361):  # Use a different variable for the inner loop
                x = h + r * math.cos(angle)
                y = k + r * math.sin(angle)
                self.points.append((x, y, z))

    def vertical_slice(self, xyz: tuple):
        z_values = [point[2] for point in self.points]
        index = bisect.bisect_left(z_values, xyz[2])

        found = []
        for point in reversed(self.points[:index]):
            if point[2] != xyz[2]:
                break
            if point == xyz:
                found.append(point)

        for point in self.points[index:]:
            if point[2] != xyz[2]:
                break
            if point == xyz:
                found.append(point)

        return found

    def get_volume(self):
        return 1 / 3 * self.circle_area * self.height


# Example usage
c = Circle(Point(0, 0), radius=1)
cone = Cone(c, height=5.000001, vertex=[0, 0, 0])
cone.get_points()

x_values, y_values, z_values = zip(*cone.points)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot the points
ax.scatter(x_values, y_values, z_values, c='r', marker='o')

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
