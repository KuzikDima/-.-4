from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Базовый класс для геометрических фигур.
    """
    def __init__(self, color: str):
        """
        Конструктор класса Shape.

        :param color: Цвет фигуры.
        """
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """
        Абстрактный метод для вычисления площади фигуры.

        :return: Площадь фигуры.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Абстрактный метод для вычисления периметра фигуры.

        :return: Периметр фигуры.
        """
        pass

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.

        :return: Строковое представление объекта.
        """
        return f"{self.color} {self.__class__.__name__}"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.

        :return: Представление объекта в виде строки.
        """
        return f"{self.color} {self.__class__.__name__}"


class Circle(Shape):
    """
    Дочерний класс для кругов.
    """
    def __init__(self, color: str, radius: float):
        """
        Конструктор класса Circle.

        :param color: Цвет круга.
        :param radius: Радиус круга.
        """
        super().__init__(color)
        self.radius = radius

    def area(self) -> float:
        """
        Метод для вычисления площади круга.

        :return: Площадь круга.
        """
        return 3.14 * self.radius ** 2

    def perimeter(self) -> float:
        """
        Метод для вычисления периметра круга.

        :return: Периметр круга.
        """
        return 2 * 3.14 * self.radius

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.

        :return: Представление объекта в виде строки.
        """
        return f"{self.color} Circle with radius {self.radius}"


class Square(Shape):
    """
    Дочерний класс для квадратов.
    """
    def __init__(self, color: str, side_length: float):
        """
        Конструктор класса Square.

        :param color: Цвет квадрата.
        :param side_length: Длина стороны квадрата.
        """
        super().__init__(color)
        self.side_length = side_length

    def area(self) -> float:
        """
        Метод для вычисления площади квадрата.

        :return: Площадь квадрата.
        """
        return self.side_length ** 2

    def perimeter(self) -> float:
        """
        Метод для вычисления периметра квадрата.

        :return: Периметр квадрата.
        """
        return 4 * self.side_length

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.

        :return: Представление объекта в виде строки.
        """
        return f"{self.color} Square with side length {self.side_length}"


if __name__ == "__main__":
    circle = Circle("red", 5.0)
    square = Square("blue", 4.0)

    print(circle)
    print("Area of the circle:", circle.area())
    print("Perimeter of the circle:", circle.perimeter())

    print(square)
    print("Area of the square:", square.area())
    print("Perimeter of the square:", square.perimeter())
