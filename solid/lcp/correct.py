class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length


def calculate_area(shape):
    return shape.area()


# Пример использования:
rectangle = Rectangle(3, 4)
square = Square(5)

print("Площадь прямоугольника:", calculate_area(rectangle))
print("Площадь квадрата:", calculate_area(square))
