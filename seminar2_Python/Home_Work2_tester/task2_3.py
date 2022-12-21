# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.

n = int(input("введите количество элементов в списке: "))
sum = 0
my_list = []
for i in range(0, n + 1):
    my_list.append((1 + 1 / n) ** n)
    sum += (1 + 1 / n) ** n
print(my_list)
print(round(sum, 2))   

