class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    @property
    def slope(self):
        if self.point2.x - self.point1.x == 0:
            raise ValueError("Slope is undefined for vertical lines.")
        return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)

    def y_intercept(self):
        return self.point1.y - self.slope() * self.point1.x

    def __repr__(self):
        return f"Line({self.point1}, {self.point2})"

A = Point(1,2)
B = Point(3,4)

slope = Line(A, B).slope