class LinearEquation:
    def __init__(self, a, b) -> None:
        self.x  = self.get_x(a, b)

    def get_x(self, a, b):
        return -(a/b)
    
a = LinearEquation(12, 10)
print(a.x)