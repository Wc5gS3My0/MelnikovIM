import numpy as np

# Функция для генерации случайных цен акций
def generate_random_prices(num_prices=100, max_price=100):
    np.random.seed(0)  # Для воспроизводимости результатов
    return np.random.rand(num_prices) * max_price

# Функция для расчета доходностей
def calculate_returns(prices):
    returns = np.diff(prices) / prices[:-1]  # Расчет доходности
    return returns

# Функция для вычисления статистических показателей
def compute_statistics(returns):
    mean_return = np.mean(returns)
    std_return = np.std(returns)
    min_return = np.min(returns)
    max_return = np.max(returns)
    return mean_return, std_return, min_return, max_return

# Основная программа
if __name__ == "__main__":
    # Генерация случайных данных для цен акций
    prices = generate_random_prices(100)  # 100 случайных цен акций от 0 до 100

    # Вычисление доходностей
    returns = calculate_returns(prices)

    # Вычисление статистических показателей
    mean_return, std_return, min_return, max_return = compute_statistics(returns)

    # Вывод результатов
    print(f"Цены акций (первые 10): {prices[:10]}")  # Вывод первых 10 цен
    print(f"Доходности (первые 10): {returns[:10]}")  # Вывод первых 10 доходностей
    print(f"Средняя доходность: {mean_return:.4f}")
    print(f"Стандартное отклонение доходности: {std_return:.4f}")
    print(f"Минимальная доходность: {min_return:.4f}")
    print(f"Максимальная доходность: {max_return:.4f}")

# Преимущества использования NumPy
#
# 1. Эффективность: NumPy оптимизирован для работы с большими объемами данных и выполняет операции быстрее, чем стандартные структуры данных Python (например, списки).
#
# 2. Удобство: Векторизированные операции позволяют писать код более лаконично и понятно.
#
# 3. Статистические функции: NumPy предоставляет множество функций для выполнения статистического анализа, что полезно в финансовых приложениях.