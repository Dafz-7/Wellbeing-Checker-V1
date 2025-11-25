import math

# Base class: Shape
class Shape:
    def __init__(self, color="red", filled=True):
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def is_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled

    def __str__(self):
        return f"Shape[color={self.color}, filled={self.filled}]"


# Circle class extends Shape
class Circle(Shape):
    def __init__(self, radius=1.0, color="red", filled=True):
        super().__init__(color, filled)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle[{super().__str__()}, radius={self.radius}]"


# Rectangle class extends Shape
class Rectangle(Shape):
    def __init__(self, width=1.0, length=1.0, color="red", filled=True):
        super().__init__(color, filled)
        self.width = width
        self.length = length

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def __str__(self):
        return f"Rectangle[{super().__str__()}, width={self.width}, length={self.length}]"


# Square class extends Rectangle
class Square(Rectangle):
    def __init__(self, side=1.0, color="red", filled=True):
        super().__init__(side, side, color, filled)

    def get_side(self):
        return self.width  # width == length

    def set_side(self, side):
        self.width = side
        self.length = side

    def set_width(self, side):
        self.set_side(side)

    def set_length(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square[{super().__str__()}]"
    
if __name__ == "__main__":
    s = Shape("blue", False)
    print(s)

    c = Circle(2.5, "green", True)
    print(c)
    print("Circle area:", c.get_area())
    print("Circle perimeter:", c.get_perimeter())

    r = Rectangle(4, 6, "yellow", True)
    print(r)
    print("Rectangle area:", r.get_area())
    print("Rectangle perimeter:", r.get_perimeter())

    sq = Square(5, "purple", False)
    print(sq)
    print("Square side:", sq.get_side())
    print("Square area:", sq.get_area())
    print("Square perimeter:", sq.get_perimeter())