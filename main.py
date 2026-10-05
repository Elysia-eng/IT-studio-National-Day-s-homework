class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r
class Square(Shape):
    def __init__(self, side）：
        self.side = side
    def area(self):
        return self.side * self.side
if __name__ == "__main__":
    shapes=[Circle(1), Square(1)]
    for shape in shapes:
        print(f"图形: {shape.__class__.__name__}, 面积: {shape.area()}")