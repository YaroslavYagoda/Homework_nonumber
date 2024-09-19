"""
Создайте базовый класс `Shape` с методом `area`, который будет возвращать площадь фигуры.
Затем создайте два подкласса `Rectangle` и `Circle`,
которые наследуют от `Shape` и переопределяют метод `area` для расчета площади прямоугольника и круга соответственно.
Создайте объекты этих классов и вызовите метод `area` для каждого из них.
"""
from math import pi


# Площадь какой фигуры должен возвращать класс Shape?
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Rectangle(Shape):
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


cl = Rectangle(2, 3)
print(cl.area())
cl = Circle(5)
print(cl.area())
