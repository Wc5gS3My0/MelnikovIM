def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
            #print(result)
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорекктный тип данных для подсчёта суммы - {i})')
    return result, incorrect_data

# numbers = "1, 2, 3"
# print(personal_sum(numbers))
def calculate_average(numbers):
    try:
        result_1 = personal_sum(numbers)
        return result_1[0] / (len(numbers) - result_1[1])
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        return print(f'В numbers записан некорректный тип данных')
    if isinstance(numbers, int):
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать