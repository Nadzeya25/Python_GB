#2 Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
print()
my_list = [2, 3, 5, 10, 6]
new_list =[]
len_new_list = len(my_list)//2 + len(my_list)%2
k = 1
for i in range (len_new_list):
   
    new_num = my_list[i] * my_list[len(my_list) - k]
    new_list.append(new_num)
    k+= 1
print(new_list)        
    