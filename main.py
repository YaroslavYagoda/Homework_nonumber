"""
Создайте базовый класс `Shape` с методом `area`, который будет возвращать площадь фигуры.
Затем создайте два подкласса `Rectangle` и `Circle`,
которые наследуют от `Shape` и переопределяют метод `area` для расчета площади прямоугольника и круга соответственно.
Создайте объекты этих классов и вызовите метод `area` для каждого из них.
"""
from math import pi


# Площадь какой фигуры должен возвращать класс Shape?
class Shape:
    def __init__(self, param1, param2=pi):
        self.param1 = param1
        self.param2 = param2

    coefficient1 = 0
    coefficient2 = 0

    def get_area(self):
        return self.coefficient1 * self.param1 ** self.coefficient2 * self.param2


class Rectangle(Shape):
    coefficient1 = 1
    coefficient2 = 1


class Circle(Shape):
    coefficient1 = 1
    coefficient2 = 2


class Triangle(Shape):
    coefficient1 = 0.5
    coefficient2 = 1


cl = Rectangle(2, 3)
print(cl.get_area())
cl = Circle(1)
print(cl.get_area())
cl = Triangle(5, 6)
print(cl.get_area())
