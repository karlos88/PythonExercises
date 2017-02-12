"""
Shape Area and Perimeter Classes - Create an abstract class called Shape and then
inherit from it other shapes like diamond, rectangle, circle, triangle etc.
Then have each class override the area and perimeter functionality to handle each shape type.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, a):
        self._a = a

    @property
    def area(self):
        return pow(self._a, 2)

    @property
    def perimeter(self):
        return self._a * 4


class Circle(Shape):
    def __init__(self, r):
        self._r = r

    @property
    def area(self):
        return self._r * pow(math.pi, 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self._r
