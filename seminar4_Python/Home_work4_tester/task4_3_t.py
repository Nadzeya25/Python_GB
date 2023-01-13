# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


import random
amount = int(input("задайте количество чисел в последовательности: "))

# 1 вариант перевода списка чисел в список строк
# for i in range(len(sum_numbers)):
#     sum_numbers[i] = str(sum_numbers[i])

# 2 вариант перевода списка чисел в список строк
# sum_numbers = [random.randint(0, amount) for i in range(amount)]
# sum_numbers = list(map(str, sum_numbers))  # map меняет тип КАЖДого элемента
# print(sum_numbers)
     
# 3 вариант перевода списка чисел в список строк
sum_numbers = list(map(str, [random.randint(0, amount) for i in range(amount)]))
sum_numbers = ''.join(sum_numbers) # склеиваем строчные элементы списка в строку через пустоту ''
print(f'задана последовательность: {sum_numbers}')
# print(type(sum_numbers))
unique_number = {}
res_nums = ''

for c in sum_numbers:
    if unique_number.get(c):
        unique_number[c] = unique_number.get(c) + 1
    else:
        unique_number[c] = 1

for k, v in unique_number.items():
    if v == 1:
        res_nums += str(k) + ' '
print(f'уникальные цифры {res_nums}') if res_nums else print('уникальных позиций нет')