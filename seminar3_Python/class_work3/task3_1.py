# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая определит, присутствует ли в заданном списке число,
# полученное от пользователя.
from random import randint       #импортируем функцию из библиотеки
n = int(input("enter a number - length of list: "))
my_list = []
for _ in range(0, n):
    my_list.append(randint(-10, 10))  #до 10 включительно
print(my_list)
find_num = int(input("введите число , которое нужно найти"))
if find_num in my_list:
    print("yes")
else:
    print("no")
# ***********************************************2 вариант через функцию
# import random  #вызов модуля точечная аннотация
from random import sample  # вызов функции sample из модуля random
           # кол-во эл-тов  #искомое число
def find_number(amount, user_number):  # создаем функцию с аргументами
    
    new_list = sample(range(1, amount+1), k=amount)  # генерирует новый список с числами от 1 до amount
                                                       #  в количестве k=amount
    print(new_list)
    if user_number in new_list:
        return "yes"
    return "no"

result_find = find_number(int(input("enter amount numbers: ")),
                          int(input("enter your number for find: ")))
print(result_find)
#****************************************** создание списка вещественных чисел
import random  #вызов модуля точечная аннотация

k = int(input("enter amount numbers: "))
some_list = [round(random.uniform(-99.999, 10), 3) for some_list in range(k)]
print(some_list)          