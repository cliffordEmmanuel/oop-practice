from cmath import pi, sqrt
import re


class Shape:
    def __init__(self, side1, side2) -> None:
        """Defines instance variables"""
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self) -> str:
        """This defines a string representation for this custom object."""

        # should be evoked with the str() function or a print()
        return f"The area of this {self.__class__.__name__} is: {self.get_area()}"


# inheriting the base class
class Rectangle(Shape):  # inherited class is in parenthesis
    pass


class Square(Rectangle):
    # implementing polymorphism ie modifying a parent method in the subclass
    # basing on the relationship that a square is a rectangle with 4 equal sides
    def __init__(self, side) -> None:
        # modifies the parent's init method to accept only one parameter
        # super() accesses the inherited class.
        super().__init__(side, side)


class Triangle(Rectangle):
    # implementing polymorphism
    def __init__(self, base, height) -> None:
        super().__init__(base, height)

    def get_area(self):
        # here we overwrite the get area method in rectangle class
        # using the relationship that the area of the triangle is
        # half that of a rectangle
        area = super().get_area()
        return area / 2


class Circle(Shape):
    """Extends the shape class"""

    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return pi * (self.radius**2)


class Hexagon(Rectangle):
    def __init__(self, side) -> None:
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * self.side**2) / 2


def compute(shape: str):
    if shape == "hexagon":
        side = float(input("What is the length of one side? "))
        hex = Hexagon(side)
        hex.get_area()
        return hex
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        circle = Circle(radius)
        circle.get_area()
        return circle
    elif shape == "triangle":
        base, height = input("What is the base and height(separated by a comma)? ").split(",")
        triangle = Triangle(float(base), float(height))
        triangle.get_area()
        return triangle
    elif shape == "square":
        side = float(input("What is the length of one side? "))
        square = Square(side)
        square.get_area()
        return square
    elif shape == "rectangle":
        length, breadth = input("What is the length and breadth(separated by a comma)? ").split(",")
        rectangle = Rectangle(float(length), float(breadth))
        rectangle.get_area()
        return rectangle


def get_menu():
    choices = {"t": "triangle", "c": "circle", "r": "rectangle", "s": "square", "h": "hexagon"}

    choice = input(
        """
    ***********************************
    Welcome to the Shape Area Calculator
    ***********************************

    To choose a particular shape, Press:

    t -> Triangle
    c -> Circle
    r -> Rectangle
    s -> Square
    h -> Hexagon
    ***********************************

    or press q to quit the program.

    """
    )

    return choices.get(choice)


def run():
    choice = get_menu()

    while choice != "q":
        area = compute(choice)
        print(area)
        choice = input("Press y to try another shape or q to quit: ")
        choice = get_menu()
        continue

    print("Thanks for trying this out!!")


def main():
    run()


if __name__ == "__main__":
    main()
