# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
from random import randint   # подключается библиотека случайных чисел
n = int(input("введите количество элементов списка: "))
position1 = int(input("введите позицию одного элемента в пределах заданного количества: "))
position2 = int(input("введите позицию другого элемента в пределах заданного количества: "))
my_list = []
for _ in range(n):
    my_list.append(randint(-n, n))
print(my_list)
if position1 < 1 or position1 > len(my_list) or position2 < 1 or position2 > len(my_list):
    print("позиции заданы некорректно")
else:
    prod_position = my_list[position1 - 1] * my_list[position2 - 1]
    print("Произведение элементов на указанных позициях равно: ", prod_position)        
