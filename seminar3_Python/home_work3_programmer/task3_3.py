#3 Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.0, 10.01] => 0.19

my_list = [2.16, 0.2, 5.1, 3.03, 10.01]

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


max_diff_min(my_list)
