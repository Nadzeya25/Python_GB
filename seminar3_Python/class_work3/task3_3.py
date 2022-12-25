# Николай Мануилов: 1. Реализуйте алгоритм задания случайных чисел
#  без использования встроенного генератора псевдослучайных чисел.

# import random  #вызов модуля точечная аннотация
from random import sample  # вызов функции sample из модуля random
k = int(input("enter amount numbers: "))
some_list = sample(range(-10, 99), k)  
print(some_list)                                                 




