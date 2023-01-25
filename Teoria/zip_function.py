# Функция zip
# Функция zip() применяется к набору итерируемых
# объектов и возвращает итератор с кортежами из
# элементов входных данных.


# Количество элементов в результате равно минимальному количеству элементов входного набора

# zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
#  ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды



users = ['user1','user2', 'user3', 'user4', 'user5']
ids = [4, 56, 66, 2, 8, 76]
data= list(zip(users, ids))   #[('user1', 4), ('user2', 56), ('user3', 66), ('user4', 2), ('user5', 8)]
salary = [111, 222, 333]
data2 =list(zip(users, ids, salary))
print(data2)  #[('user1', 4, 111), ('user2', 56, 222), ('user3', 66, 333)]  - 3 котрежа

# собираются парами или  тройками(группами) в виде кортежей.
#  Количество кортежей определяется по наименьшему списку данных