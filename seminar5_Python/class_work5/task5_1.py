# (Maria Andreeva)1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.
# формируем список по условию задачи без одного элемента
from random import choice  
#функция ****choice**** берет из списка случайное значение
# *****remove***** его удаляет
def invalid_list(num):
    any_list = list(range(0, num + 1))
    any_list.remove(choice(any_list))
    return any_list

def find(any_list):
    for i in range(1, len(any_list)):
        if any_list[i] - 1 != any_list[i-1]:
            return any_list[i] -1  
    return -1
my_list = invalid_list(int(input("введите число: ")))
print(my_list)   
print(find(my_list))

# *******НИКОЛАЙ******Среди чисел не хватает одного,
#  чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

data = '1 2 3 4 5 6 8 9 10 '
num_row = []
for line in data:
        num_row += list(map(int, line.split()))
print(num_row)
for i, elem in enumerate(num_row[:-1]):
    if elem + 1 != num_row[i+1]:
        print(elem + 1)
        break

num_list = [1, 5, 2, 3, 4, 6, 1, 7]
print(num_list, end=' => ')

min_num = num_list[0]

for i in range(len(num_list)):
    order_list = []
    order_list.append(num_list[i])
    min_num = num_list[i]
    for j in range(i,len(num_list)-1):
        if num_list[j] > min_num:
            min_num = num_list[j]
            order_list.append(num_list[j])
if len(order_list) > 1:
    print(order_list, end=' ')  