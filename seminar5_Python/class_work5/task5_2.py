# 2. **********maria**********Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя

from random import choices 

# функция ****choices****

#  возвращает !!!!список!!! элементов длины k ,
#  выбранных из последовательности (список- any_list или кортеж -any_tuple ....или  range(1, num*2)....) 
# с перестановкой элементов.
#  Другими словами, функция используется,
#  когда требуется выбрать несколько k случайных элементов
#  из заданной последовательности,
#  элементы не сохраняют первоначальный порядок.

def any_list(num):
    return choices(range(1, num*2), k=num) #  k - количество выбираемых случайных элементов


def seq(some_list):
    temp_list =[]
    for i in range(len(some_list)):
        num_1 = some_list[i]
        out_list = [num_1]
        for j in range(i+ 1, len(some_list)):
            if some_list[j] > num_1:
                num_1 = some_list[j]
                out_list.append(num_1)
        if len(out_list) > 1:          #условие, по которому к большому итоговому списку(temp_list)
                                                #  добавляем только те подсписки(out_list),
                                                #  длина которых больше одного
            temp_list.append(out_list)       
    return temp_list
my_list =  any_list(10)  
print(my_list)  
# print(seq(my_list))
exit()
# **********nikolai****************************************
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

