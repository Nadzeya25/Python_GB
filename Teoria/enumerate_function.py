# Функция enumerate
# Функция enumerate() применяется к итерируемому
# объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.


# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
#  ↓
# [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# Нельзя пройтись дважды


# users = ['user1','user2', 'user3', 'user4', 'user5']
# data = list(enumerate(users))
# print(data) #[(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

list1 = [12, 23, 44, -6, 0, -8, 5, 100]

list2 = []
for el in list1:            # пробегаемся по элементам, получаем нужные элементы
    if el > 10:
        list2.append(el)
print(list2)

list3 = []                     #  пробегаемся по индексам, получаем список нужных индексов
for i in range(len(list1)):
    if  list1[i] > 0:
        list3.append(i)
print(list3)

list4 = []
for i, v in enumerate(list1):           # пробегаемся по парам  - индекс/элемент, берем, что надо
    if  v > 0:
        list4.append(v)
print(list4)
