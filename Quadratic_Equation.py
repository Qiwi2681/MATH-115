from Point import Point
import matplotlib.pyplot as plt
import numpy as np

class Parabola:
    """Object representing a parabola"""
    def __init__(self, x_vals):
        self.x = x_vals
        self.y = []
        self.discriminant = None
        self.a = None
        self.b = None

    def get_points(self, a, b, c):
        self.get_y_vals(a, b, c)
        points = [Point(x_y[0], x_y[1]) for x_y in zip(self.x, self.y)]
        return points

    def get_y_vals(self, a, b, c):
        self.a = a
        self.b = b
        self.discriminant = (b**2)-(4*a*c)
        for x in self.x:
            self.y.append(a * x**2 + b * x + c)

x_values = [x for x in range(-500, 500, 5)]
parabola = Parabola(x_values)
points = parabola.get_points(3, 5, -8)

for point in points:
    print(f"Point: ({point.x}, {point.y})")
print(parabola.discriminant)

# Create 64 parabolas with coefficients a and b ranging from -4 to +4, and c set to 0
num_parabolas = 81
x_values = np.linspace(-10, 10, 100)
parabolas = []

# Iterate through all combinations of a and b
for a in range(0, 10):
    for b in range(0, 10):
        c = 1
        parabola = Parabola(x_values)
        parabola.get_y_vals(a, b, c)
        parabolas.append(parabola)

# Plot all 64 parabolas
plt.style.use("seaborn-v0_8")

fig, axs = plt.subplots(9, 9, figsize=(18, 18), sharex=True, sharey=True)

for i in range(num_parabolas):
    row, col = divmod(i, 9)
    axs[row, col].plot(parabolas[i].x, parabolas[i].y, linewidth=2.0)
    axs[row, col].set_title(f'a={parabolas[i].a:.2f}, b={parabolas[i].b:.2f}, D={parabolas[i].discriminant}')

plt.tight_layout()
plt.show()