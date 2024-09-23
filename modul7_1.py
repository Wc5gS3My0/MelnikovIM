from itertools import product


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            products = file.read()
            file.close()
            return products
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = self.get_products(),
        existing_names = {line.split(',')[0] for line in existing_products if line}

        for product in products:
            if product.name in existing_names:
                print(f'Продукт {product} уже есть в магазине')
            else:
                file = open(self.__file_name,'a')
                file.write(str(product)+'\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())