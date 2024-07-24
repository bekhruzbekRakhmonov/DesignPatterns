from abc import ABC, abstractmethod
import math

class Triangle:
    @abstractmethod
    def calculate_perimetr(self) -> float:
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass

class RightTriangle(Triangle):
    """
    a,b,c - the side of triangle
    h - height of triangle
    """
    a: float
    b: float
    c: float

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimetr(self) -> float:
        return self.a + self.b + self.c

    def calculate_area(self) -> float:
        if (self.a**2) + (self.b**2) != self.c**2:
            raise Exception("This is not right triangle")

        area = (self.a * self.b) / 2
        return area

class EquilateralTriangle(Triangle):
    """
    a,b,c - the side of triangle
    h - height of triangle
    """
    a: float

    def __init__(self,a):
        self.a = a

    def calculate_perimetr(self) -> float:
        return self.a * 3

    def calculate_area(self) -> float:
        area = ((3**1/2) * (self.a**2)) / 4
        return area

class DifferentTriangle(Triangle):
    """
    a,b,c - the side of triangle
    h - height of triangle
    """
    a: float
    b: float
    c: float

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimetr(self) -> float:
        return self.a + self.b + self.c

    def calculate_area(self) -> float:
        hp = self.calculate_perimetr() / 2 # half of perimetr
        area = (hp * (hp-self.a) * (hp-self.b) * (hp-self.c)) ** 1/2 # geron formula
        return area

def main():
    # triangle = EquilateralTriangle(4,5,8)
    # triangle = DifferentTriangle(4,5,8)
    triangle = RightTriangle(4,5,8)
    perimetr = triangle.calculate_perimetr()
    area = triangle.calculate_area()
    print(perimetr)
    print(area)

if __name__ == "__main__":
    main()
