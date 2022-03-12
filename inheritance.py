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
        print("color:", self.color)


class Circle2(GeometricObject):

    def __init__(self, color, line_width, radius):
        super().__init__(color, line_width)
        self.radius = radius
        super().introduce()

    def introduce(self):
        print("from circle2")
        super().introduce()



class Rectangle2(GeometricObject):

    def __init__(self, color, line_width, width, height):
        super().__init__(color, line_width)
        self.width = width
        self.height = height


c = Circle2("white", 2, 5)
print(c.color)
c.introduce()