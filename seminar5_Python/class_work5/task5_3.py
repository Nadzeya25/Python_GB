# удалить из строки все слова , содержащие абв 
my_str = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абВ'
new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))
print(new_str)










#Задача из 6 семинара************ Напишите программу вычисления арифметического
# выражения заданного строкой. Используйте операции
# +,-,/,* приоритет операций стандартный. 
# * Добавьте скобки,  приоритет операций меняется.

# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
# exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
# actions = {
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
# }
