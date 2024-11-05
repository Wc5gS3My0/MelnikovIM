# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка, высчитывающая разницу длин строк, если их длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка, сравнивающая длины строк на одинаковых позициях без использования zip
second_result = (len(first[i]) != len(second[i]) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))  # Преобразуем генератор в список для вывода
print(list(second_result))  # Преобразуем генератор в список для вывода
