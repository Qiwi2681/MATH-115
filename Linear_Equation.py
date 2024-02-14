class LinearEquation:
    def __init__(self, a, b) -> None:
        # Check if b is zero to avoid division by zero
        if b == 0:
            raise ValueError("The value of 'b' cannot be zero.")
        self.slope = self.get_slope(a, b)
        self.x_intercept = self.get_x_intercept(a, b)

    def get_slope(self, a, b):
        return -(a / b)

    def get_x_intercept(self, a, b):
        return -b / a if a != 0 else None  # Handle the case where a is zero

# Example usage
equation = LinearEquation(12, 10)
print("Slope:", equation.slope)
print("X-intercept:", equation.x_intercept)
