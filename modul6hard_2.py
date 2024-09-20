class Figure:
    def __init__(self, rgb, *sides):
        self.color = list(rgb)
        self.sides = list(sides)
        self.filled = True

    def get_color(self):
        return self.color

    def _is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [r, g, b]

    def _is_valid_sides(self):
        return all(side > 0 and isinstance(side, (int, float)) for side in self.sides)

    def set_sides(self, *args):
        self.sides = list(args)
        if not self._is_valid_sides():
            raise ValueError("Invalid sides")

    def get_sides(self):
        return self.sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, radius):
        super().__init__(rgb, radius)
        self.radius = radius

    def get_area(self):
        return 3.14159 * (self.radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, side):
        super().__init__(rgb, side, side, side)  
        self.side = side

    def get_area(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, side):
        super().__init__(rgb, side)
        self.side = side

    def get_volume(self):
        return self.side ** 3

# Пример использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 100), 10)

# Проверка изменения цветов
circle1.set_color(55, 66, 77)  
print(circle1.get_color())  

cube1.set_color(300, 70, 15)  
print(cube1.get_color())  

# Проверка изменения сторон
cube1.set_sides(6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)  
print(cube1.get_sides())  

circle1.set_sides(15) 
print(circle1.get_sides())  

# Проверка площади (для треугольника)
print(triangle1.get_area()) 

# Проверка объема (куба)
print(cube1.get_volume())  
