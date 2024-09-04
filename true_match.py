from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second

result3 = divide(49, 7)
result4 = divide(15, 0)
print(result3)
print(result4)