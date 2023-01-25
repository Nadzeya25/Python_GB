# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011


def convert_int(num : int):
    my_list = []
    while num > 0 :
        my_list.insert(0, num % 2)
        num = num//2
    print(*my_list, sep="")            # звездочка распаковывает список, sep="" без пробелов
# num = int (input("enter number: "))
# convert_int(num)