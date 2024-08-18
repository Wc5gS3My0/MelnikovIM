def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(78, 'rabid', False)
print_params(589, 'Rom')
print_params(b = 'Норвегия')
print_params(b = 25)
print_params(c = [1, 2, 3])

values_lict = [55,"Home",55.66]

values_dict = {'a':58, 'b':'Black', 'c':False}

print_params(*values_lict)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)




