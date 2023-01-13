# * 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (от -10 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0


import random
def createDict():   #создаем словарь, где ключ- это степень, а значение  - это коэффициент при x
    equation = {}
    degree = int(input('Введите максимальную степень многочлена: '))
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-10,10)
    return equation
my_dict = createDict()
print(my_dict)
# ***************************************************************************************************************************
def createEquation(equation: dict): #созд строку на основе словаря- из  ключей и значений с нужными знаками + -
    strEquation = ''
    first = True

    for k,v in equation.items():                       
        if first:
            first = False                            # убираем плюс перед первым членом, расставляем пробелы
            if v > 0:
                strEquation += f'{v}*x^{k}'
            elif v < 0:
                strEquation += f'-{abs(v)}*x^{k}'
        else:
            if v > 0:
                strEquation += f' + {v}*x^{k}'     # если  v ноль , то не добавляет член в многочлен,    
            elif v < 0:                            # поэтому elif, а не else
                strEquation += f' - {abs(v)}*x^{k}'

    return strEquation
my_string = createEquation(my_dict)
print(my_string)
# *******************************************************************************************************************************
def printEquation(equation: str):  # приводим первую и нулевую степень к другому виду, и "= 0" в конце
    out_string = (equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0\n')
    return out_string

# *****************************************************************************************************************************




# def pars_equation(equation: str):   #создаем словарь из строки с многочленом
#     dict_equation = {}
#     # группируем    
#     equation = equation.replace(' + ', ' ').replace(' - ', ' -').replace('- ', '-')
#     # print(strEquation)
#     # собираем список сгруппированных элементов, "сплитуем" по пробелам
#     equation = equation.split(" ")
#     # print(listEquation)
#     for i in equation:
#         element = i.split("*x^")
#         dict_equation[int(element[1])] = int(element[0])

#     return dict_equation

# my_Equation1 = createDict()
# my_Equation2 = createDict()


# def summ_equation(Equation1: dict, Equation2: dict):  # создаем словарь сложением двух словарей
#     final_equation = {} 
#     for i in range(max(len(Equation1),len(Equation2)), -1, -1):
#         if Equation1.get(i) or Equation2.get(i):
#             final_equation[i] = (Equation1.get(i) if Equation1.get(i) else 0) + (Equation2.get(i) if Equation2.get(i) else 0)
#     return final_equation
# sum_my_Equations = summ_equation(my_Equation1, my_Equation2) 
# # print(sum_my_Equations)   
# my_strEquation = createEquation(my_dict)
# print(my_strEquation)

# # printEquation(createEquation(my_Equation1))
# # printEquation(createEquation(my_Equation2))
# # printEquation(createEquation(sum_my_Equations)) # получаем красивый многочлен
my_finish_string = printEquation(my_string)
print(my_finish_string)

f = open(r"C:\Users\lustr\OneDrive\Документы\Python_GB\seminar4_Python\Home_work4_tester\file1.txt", "w") 
f.write(my_finish_string*3) # записала строку с многочленом в файл