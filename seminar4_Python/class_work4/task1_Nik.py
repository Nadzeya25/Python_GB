# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.

#1 способ: задать список из чисел
my_list_str = input("Введите числа через пробел").split()  # split - делает список строк из вводимых

# 2 способ:
# сделать список строк из готовой строки
my_str = "25 56 32 11"
my_list_str = my_str.split(" ")
print(my_list_str)
# сделать числовой список из списка строк
my_list_nums = list(map(int, my_list_str)) # преобразует список строк в список int чисел
print(my_list_nums)


#********************************** 1 способ по задаче
min_num = min(my_list_nums)
max_num = max(my_list_nums)
print(min_num, max_num)

#*************************************** 2 способ по задаче
def max_min_num(any_list):
    max_num = min_num = any_list[0]
    for num in any_list:
        if max_num < num:
            max_num = num
        elif min_num > num:
            min_num = num
    print(f"min =  {min_num}  max = {max_num}") 
       
max_min_num(my_list_nums)