# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# in 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

print()
my_list = [2, 2, 4, 8, 8]
new_list =[]
len_new_list = len(my_list)//2 + len(my_list)%2

for i in range (len_new_list):
    new_num = my_list[i] * my_list[- 1 - i]
    new_list.append(new_num)
  
if len(my_list)%2 != 0:
    new_list[len_new_list - 1] = my_list[len(my_list)//2]    

print(new_list)       
