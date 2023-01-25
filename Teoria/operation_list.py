# операции со списками

list2 = [4, 5, 8, 54, -8, 7, -9]
list3 = ['jh', 'o', 'i', 25, 88, '%%']
5 in list2 #— true, если элемент x есть в списке l;
-9 not in list2 #— true, если элемент x отсутствует в l;
list2 + list3 #— объединение двух списков;
#list2 * n , n * list2 #— копирует список n раз;

                                               # функции

len(list2) #— количество элементов в списке;
min(list2) #— наименьший элемент;
max(list2) #— наибольший элемент;
sum(list2) #— сумма чисел списка, только, если все элементы int;
print(sum(list2))
print(list2 + list3)
del list2[2] #- удалить элемент списка по индексу 2
sorted() #- сортировка, изначальный список не меняется*****
sorted(a,reverse=True) #- сортировка по убыванию
sorted(list2) #- можно применять к любым итерабельным последовательностям(всё что можно обойти в цикле for)
#  но вернет все равно список

# эта функция не изменяет сортируемый список, а все отсортированные элементы она помещает в новый список,
#  который возвращается в качестве результата, .
people = ["Tom", "bob", "alice", "Sam", "Bill"]
sorted_people = sorted(people, key=str.lower)
print(sorted_people)      # ["alice", "Bill", "bob", "Sam", "Tom"]
# либо список переназначается
people2 = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people2 = sorted(people2)
print(people2)      # ["Alice", "Bill", "Bob", "Sam", "Tom"]
# ***********************************************************************************************************
                                 #  МЕТОДЫ списков Python
      # .index

# Возвращает индекс первого совпавшего элемента. Поиск совпадения происходит слева направо. Пример:
numbers = [1, 5, 9, 6, 1, 2, 1]
print(numbers.index(1))
# вывод 0: первая найденная единица на позиции 0

       # .count

# Данный метод считает, сколько раз указанное значение появляется в списке Python:
numbers = [1, 5, 9, 6, 1, 2, 1]
print(numbers.count(1))
# вывод 3, потому что единица встречается 3 раза

      # .append

# Добавляет указанное значение в конец:
numbers = [1, 5, 9, 6]
numbers.append(3)
# обновлённый список: [1, 5, 9, 6, 3]

                #  .sort()  изменяет список

.sort() #- метод сортирует список по возрастанию, ********изменяя изначальный список******
.sort(reverse=True) #- сортирует список по убыванию
.reverse() #-  в обратном порядке список  - так же это можно сделать a[::-1]
.sort #метод применяется только в списках

people2 = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people2.sort()
print(people2)      # ["Alice", "Bill", "Bob", "Sam", "Tom"]

#https://metanit.com/python/tutorial/3.1.php

#https://github.com/iStoriesMedia/python_lessons/blob/main/%D0%A3%D1%80%D0%BE%D0%BA%209.%20%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0.ipynb



people = ["Tom", "Bob"]

# добавляем в конец списка
people.append("Alice")  # ["Tom", "Bob", "Alice"]

# добавляем на вторую позицию
people.insert(1, "Bill")  # ["Tom", "Bill", "Bob", "Alice"]

# добавляем набор элементов ["Mike", "Sam"]
people.extend(["Mike", "Sam"])      # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]

# возвращает индекс элемента в виде инт числа
index_of_tom = people.index("Tom")



# удаляем по этому индексу возвращает удаленное значение
removed_item = people.pop(index_of_tom)     # ["Bill", "Bob", "Alice", "Mike", "Sam"]

# удаляем элемент - по умолчанию последний(возвращает значение удаленного элемента)
last_item = people.pop()     # ["Bill", "Bob", "Alice", "Mike"]

# удаляем элемент "Alice" первое его вхождение
people.remove("Alice")      # ["Bill", "Bob", "Mike"]
print(people) 

#  Метод ***.pop*** удаляет элемент по индексу. При этом возвращает удаленное из списка значение в программу.
#  Метод ***.remove*** принимает значение удаляемого элемента, и удаляет первое его вхождение.
#  Если элемента нет в списке, возникает исключение ValueError .


# удаляем все элементы
people.clear()
print(people)      
                        # оператор del

people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
 
del people[1]   # удаляем второй элемент
print(people)   # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]
del people[:3]   # удаляем  по четвертый элемент не включая
print(people)   # ["Bill", "Kate", "Mike"]
del people[1:]   # удаляем  со второго элемента
print(people)   # ["Bill"]


" ".join(words)
# из СПИСКА строк делает строку
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
 
# разделитель - пробел
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English

# Перебор элементов
# Для перебора элементов можно использовать как цикл for, так и цикл while.

# Перебор с помощью цикла for:
people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)
# Здесь будет производиться перебор списка people,
#  и каждый его элемент будет помещаться в переменную person.

# Перебор также можно сделать с помощью цикла while:
people = ["Tom", "Sam", "Bob"]
i = 0
while i < len(people):
    print(people[i])    # применяем индекс для получения элемента
    i += 1
# Для перебора с помощью функции len() получаем длину списка.
#  С помощью счетчика i выводит по элементу,
#   пока значение счетчика не станет равно длине списка.

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

