from inheritance import *


def addCircle(lst: list, c: Circle2):
    if isinstance(c, Circle2):
        lst.append(c)
    else:
        raise Exception("wrong type")


def addRectangle(lst: list, r: Rectangle2):
    if isinstance(r, Rectangle2):
        lst.append(r)
    else:
        raise Exception("wrong type")


circle_list = []
addCircle(circle_list, Circle2("white", 2, 2))
addCircle(circle_list, Circle2("white", 2, 3))
addCircle(circle_list, Circle2("white", 2, 4))
addCircle(circle_list, Circle2("white", 2, 5))

rect_list = []
addRectangle(rect_list, Rectangle2("black", 2, 1, 20))
addRectangle(rect_list, Rectangle2("black", 2, 1, 30))
addRectangle(rect_list, Rectangle2("black", 2, 1, 40))
addRectangle(rect_list, Rectangle2("black", 2, 1, 50))


def addGeometricObject(lst: list, go: GeometricObject) -> None:
    if isinstance(go, GeometricObject):
        lst.append(go)
    else:
        raise Exception("wrong type")


go_list = []
addGeometricObject(go_list, GeometricObject("white", 2))
addGeometricObject(go_list, Circle2("red", 1, 7))
addGeometricObject(go_list, Rectangle2("pink", 2, 1, 70))

for i in go_list:
    i.introduce()
    print()

# addRectangle(rect_list, Circle2("red", 1, 1))
# for i in rect_list:
#     i.introduce()

# addGeometricObject(go_list, Rectangle("pink", 1, 2, 3))
# addGeometricObject(go_list, Circle("pink", 1, 2, 3))


def calculateDistanceOfPoints(x1: float, y1: float, x2: float, y2: float) -> float:
    pass


