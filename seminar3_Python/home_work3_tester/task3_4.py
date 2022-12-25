# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным
#   и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
import random  #вызов модуля точечная аннотация

k = int(input("enter amount numbers: "))
some_list = [round(random.uniform(-9.999, 10), 2) for some_list in range(k)]
print(some_list)                                                 

# генерирует новый список с числами от n до m
#  в количестве k
def max_diff_min(my_list: list):
    num_max = num_min = (my_list[0]) % 1
    for i in range(1, len(my_list)):
        num = round((my_list[i]) % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
    return result


max_diff_min(some_list)