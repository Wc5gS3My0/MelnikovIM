# Неизменяемые и изменяемые объекты. Кортежи.
immutable_var=(45.66,5588,'Человек невидимка', set)
print(immutable_var)

#immutable_var=(45.66,5588,'Человек невидимка', set)
#print(immutable_var)
#immutable_var(2)=854# mне поддерживает обращение элементов
#print(immutable_var)

mutable_list=('apple','orange','banana', 548, float)
print(mutable_list)
mutable_list=('apple','orange','banana', 555, float)
print(mutable_list[2])