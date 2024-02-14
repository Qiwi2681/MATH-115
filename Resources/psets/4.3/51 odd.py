from Point import Point
from math import sqrt

def f():
    a = 2
    b = -1
    c = 2

    def x(x):
        return a*(x**2) + b * x + c

    # a)
    def vertex():
        delta = (-b)/(2*a)
        # 1 /4
        return Point(delta, x(delta))
    
    vertex = vertex()
    print(f'Vertex at: ({vertex.x}, {vertex.y})')
    print(f'Axis of Symmetry: {vertex.x}')

    if a > 0:
        print('Concave Down')

    #b
    def d():
        # b: 1
        # -
        # 16
        #root 15 > 0 so 2 solutions
        return sqrt((b**2) - (4*a*c)) 
    
    # -1 + root 15 /4
    pos = (-b + d())/(2*a)

f()
