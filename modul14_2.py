import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
conn.commit()
#for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age,balance) VALUES (?, ?, ?, ?)'
#                    , (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))

#for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))

#for i in range(1, 11, 3):
# cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age <> 60')
#rows = cursor.fetchall()
#for row in rows:
#     print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')

# Удаление пользователя с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчет общего количества пользователей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Проверка на случай, если нет пользователей
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0  # Если пользователей нет, средний баланс 0

average_balance = round(average_balance, -2)

# Вывод среднего баланса
print(average_balance)

# Закрытие соединения с базой данных
conn.close()