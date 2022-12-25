# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in -> 5
# out ->[10, 2, 3, 8, 9]  -> 22
# in -> 4
# out -> [4, 2, 4, 9] -> 8

my_list = []
n_len = int(input("enter amount numbers: "))
from_num = int(input("enter start num list: "))
to_num = int(input("enter stope num list: "))

# функция для создания списка чисел с помощью randint
from random import randint
def init_new_list (some_list, list_len, start_num, stope_num ): 
    for i in range (list_len):
        some_list.append(randint(start_num, stope_num))
    print(some_list)

init_new_list(my_list, n_len, from_num, to_num )
print()

sum_positiv = 0
for i in range(n_len):
    if i % 2 == 0:  # нечетные позиции - это четные индексы, ноль - тоже четное число
        sum_positiv += my_list[i]
  
print(sum_positiv)
print()

