# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
#  значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

# образец
# С помощью list comprehensions создайте второй массив,
# где на четных индексах будут находиться соответствующие элементы массива mas,
# умноженные на 10, а на нечетных индексах -- единицы.
# m = [13, 3, 16, 2, 5, 18]
# mas = [m[x] * 10 if not x % 2 else 1 for x in range(len(m))]
# print(mas)  #[130, 1, 160, 1, 50, 1]
# exit()


import random
my_list = [random.randint(0, 30) for _ in range(int(input("введите количество чисел в задаваемом списке: ")))]
print(my_list)

def gen_new_list(any_list):
    res_list = []
    for i in range(1,len(any_list)):
        if any_list[i] > any_list[i-1]:
            res_list.append(any_list[i])
    return res_list
# print(gen_new_list(my_list))

res_list = [my_list[i] for i in range(1,len(my_list)) if my_list[i] > my_list[i-1]]
print(res_list)

# пример из интернета
# a = [13, 3, 16, 2, 5, 18]
# m = [j for i, j in zip(a, a[1:]) if j > i]
# print(a)
# print(a[1:])
# print(list(zip(a, a[1:])))
# print(m)


