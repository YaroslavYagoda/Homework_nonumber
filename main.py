"""
Создайте базовый класс `Shape` с методом `area`, который будет возвращать площадь фигуры.
Затем создайте два подкласса `Rectangle` и `Circle`,
которые наследуют от `Shape` и переопределяют метод `area` для расчета площади прямоугольника и круга соответственно.
Создайте объекты этих классов и вызовите метод `area` для каждого из них.
"""
from math import pi


class Shape:
    def area(self, b, a):
        return a * b


class Rectangle(Shape):
    def area(self, a, b):
        return a * b


class Circle(Shape):
    def area(self, r):
        return pi * r ** 2


cl = Rectangle()
print(cl.area(2, 3))
cl = Circle()
print(cl.area(5))
