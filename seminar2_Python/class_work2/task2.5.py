from random import randint

number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)//2):
    number = number - 1
    a = list[i] * list[number]
    list2.append(a)
    i += 1
    middle = [int(list[i])]
list3 = list2+middle
if len(list) % 2 == 0:
    print(list)
    print(list2)
else:
    print(list)
    print(list3)