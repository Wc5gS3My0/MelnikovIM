# словари и множества
#работа со словорями
my_dict={'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict['Egor'])
print(my_dict.get('Inna'))
my_dict.update({'Kamila' : 1981, 'Artem' : 1915})
print(my_dict)
a=my_dict.pop('Vasya')
(my_dict)
print(a)
print(my_dict)

#работа с множеством
my_set={1,1,1,1,1,1, 'Яблоко', True, 42.314,(5,6,9)}
print(my_set)
my_set.update({8,8,8,8,8, 'Пиво'})
print(my_set)
list={1, 'Пиво', 8, 42.314, 'Яблоко',(5,6,9)}
print(list)
print(list.discard(1))
print(list)



