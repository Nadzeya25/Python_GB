# import random  #вызов модуля точечная аннотация
from random import sample  # вызов функции sample из модуля random
k = int(input("enter amount numbers: "))
some_list = sample(range(-10, 99), k)  
print(some_list)                                                 

# генерирует новый список с числами от n до m
#  в количестве k
#**********************************************создание списка вещественных чисел
import random  #вызов модуля точечная аннотация

k = int(input("enter amount numbers: "))
some_list = [round(random.uniform(-99.999, 10), 3) for some_list in range(k)]
print(some_list)          