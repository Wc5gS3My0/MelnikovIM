# арифметика
"1st program"
print((9**0.5)*5)

# сравнение, or, and.
"2nd program"
print(99.9>99.8 and 1000!=1001)

# сложная арифметика
("3rd program")
print(int(1234%1000//10) + (5678%1000//10))

# все, везде и сразу.
num1=13.42
num2=42.13

num1_int, num1_float = int(num1), num1 % 1
num2_int, num2_float= int(num2), num2 % 1

result = num1_int==num2_float or num2_int==num1_float
print(result)