import math

class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.color = color
        self.sides = []
        self.filled = False
        self.__sides = []
        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = (r, g, b)
        else:
            raise ValueError("Invalid color value")

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return len(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            raise ValueError("Invalid sides")

class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3

# Примеры использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(255, 70, 15)  # Убедитесь, что цвет корректен
print(cube1.get_color())

cube1.set_sides(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)  # Устанавливаем 12 сторон
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))  # Вывод длины sides
print(cube1.get_volume())  # Объем куба
