n = int(input("Введите число n (от 3 до 20): "))

def generate_password(n):
    password = []

    for i in range(1, n):
        for j in range(i + 1, n):
            if i + j == n and i not in [pair for pair in password for number in pair]:
                password.append((i, j))

    return password

password = generate_password(n)


result = "".join([str(pair[0]) + str(pair[1]) for pair in password])

print(f"Пароль для числа {n}: {result}")