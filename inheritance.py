"""
    Neden inheritance?:
        1. Code reusability
        2. Maintainance
        3. More Debuggable code
"""


# inheritance olmadan

class Circle:

    def __init__(self, color, line_width, radius):
        self.color = color
        self.line_width = line_width
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle:

    def __init__(self, color, line_width, width, height):
        self.color = color
        self.line_width = line_width
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


# inheritance ile

class GeometricObject:

    def __init__(self, color, line_width):
        self.color = color
        self.line_width = line_width

    def introduce(self):
        print("color:", self.color, ", line width:", self.line_width, end=" ")


class Circle2(GeometricObject):

    def __init__(self, color, line_width, radius):
        super().__init__(color, line_width)
        self.radius = radius

    def introduce(self):
        super().introduce()
        print("radius:", self.radius)


class Rectangle2(GeometricObject):

    def __init__(self, color, line_width, width, height):
        super().__init__(color, line_width)
        self.width = width
        self.height = height

    def introduce(self):
        super().introduce()
        print("width:", self.width, "height:", self.height)


# c = Circle2("white", 2, 5)
# print(c.color)
# c.introduce()
