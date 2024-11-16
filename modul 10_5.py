import os
import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая пробелы
    print(f"Файл {name} считан, строк: {len(all_data)}")


if __name__ == '__main__':
    print("Текущая директория:", os.getcwd())  # Выводим текущую директорию

    # Список названий файлов (пример, измените на свои имена файлов)
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейное время выполнения: {linear_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.time() - start_time
    print(f"Многопроцессное время выполнения: {multiprocess_time:.6f} секунд")
