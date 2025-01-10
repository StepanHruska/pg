# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.
import math

class Shape():

    def area(self):
        return 0.0

# ZDE DOPLŇTE VLASTNÍ KÓD
class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    def area(self):    
        Rectangle.area = self._height * self._width
        return Rectangle.area
    
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius 
        Circle.area = math.pi* (self._radius**2)

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
   assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3