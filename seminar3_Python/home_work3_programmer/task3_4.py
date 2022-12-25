# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def convert_int(num : int):
    my_list = []
    while num > 0 :
        my_list.insert(0, num % 2)
        num = num//2
    print(*my_list, sep="")

convert_int(int (input("enter number: ")))    
     
