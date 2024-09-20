"""
Создайте базовый класс `Shape` с методом `area`, который будет возвращать площадь фигуры.
Затем создайте два подкласса `Rectangle` и `Circle`,
которые наследуют от `Shape` и переопределяют метод `area` для расчета площади прямоугольника и круга соответственно.
Создайте объекты этих классов и вызовите метод `area` для каждого из них.
"""
from math import pi


class Shape:
    def get_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height * 0.5


cl = Rectangle(2, 3)
print(cl.get_area())
cl = Circle(5)
print(cl.get_area())
cl = Triangle(5, 6)
print(cl.get_area())
