# 3. На вход программе подается число n.
#    Программа печатает численный треугольник.
#    Используем вложенные циклы.

# iteration = int(input("Введите число -> "))
# for i in range(1, iteration+1):
#     for k in range(i):
#         print(i, end='')
#     print()
# a = [1, 5, 8, 9]
# help(a.copy)
#***************************************** импорт функции из соседнего файла
# import task4_2
# num1 = 24
# print(task4_2.convert_int(num1))
#**********************************************рекурсия Фибоначчи из лекции 2
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

my_list = []
for e in range(1, 7):
    my_list. append(fib(e))
print(my_list)
