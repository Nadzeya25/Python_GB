# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

n = int(input("введите число: "))
n_mod = abs(n)  # модуль числа
my_list = list(range(n_mod * -1, n_mod + 1))  # функция list создает список 
print(my_list)
print("количество элементов получившегося списка равно:", len(my_list))

position1 = int(input("введите позицию одного элемента : "))
position2 = int(input("введите позицию другого элемента : "))

if position1 < 1 or position1 > len(my_list) or position2 < 1 or position2 > len(my_list):
    print("позиция отсутствует в списке")
else:
    prod_position = my_list[position1 - 1] * my_list[position2 - 1]
    print("Произведение элементов на указанных позициях равно:", prod_position)        
