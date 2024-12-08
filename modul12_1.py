import unittest

# Предполагается, что класс Runner уже определен в этом файле или импортирован из другого модуля

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        rn = Runner(name='Бегунъ')
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)  # Проверяем, что расстояние равно 50

    def test_run(self):
        rn = Runner(name='Бегунъ')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)  # Проверяем, что расстояние равно 100

    def test_challenge(self):
        rn1 = Runner(name='Бегунъ')
        rn2 = Runner(name='Спортсмен')
        for _ in range(10):
            rn1.run()
        for _ in range(10):
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)  # Проверяем, что расстояния не равны

if __name__ == '__main__':
    unittest.main()
