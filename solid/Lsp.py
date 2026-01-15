from typing import List
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Rectangle class
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Calculate rectangle area
    def calculate_area(self):
        return self._width * self._height


# Square class, inherits from Rectangle
class Square(Figure):
    def __init__(self, side):
        self.side = side

    # Calculate square area
    def calculate_area(self):
        return self.side * self.side


# Function to calculate total area of multiple rectangles
def calculate_total_area(rects: List[Rectangle]):
    total_area = 0
    for obj in rects:
        total_area += obj.calculate_area()
    return total_area


figures = [Rectangle(5, 6), Square(10)]
print(calculate_total_area(figures))
