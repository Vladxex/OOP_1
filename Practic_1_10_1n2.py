
class Rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def getRect(self):

        return "Rectangle ({}, {}, {}, {})" .format(self.x, self.y, self.width, self.height)
    def getArea(self):
        return self.width * self.height


recta = Rectangle(5, 10, 50, 100)

print(recta.getRect())
print(recta.getArea())
