# 4. Напишите программу, которая по заданному номеру четверти, 
#  показывает диапазон возможных координат точек в этой четверти (x и y). 
num_quarter = int(input("введите номер четверти (от 1 до 4): ")) 
while num_quarter < 1 or num_quarter > 4: 
    print("ошибка ввода") 
else:  
    if num_quarter == 1: 
        print("значения координат точек в " + str(num_quarter) + " четверти  будут x > 0, y > 0") 
    elif num_quarter == 2: 
        print("значения координат точек в " + str(num_quarter) + " четверти  будут x < 0, y > 0") 
    elif num_quarter == 3: 
        print("значения координат точек в " + str(num_quarter) + " четверти  будут x < 0, y < 0") 
    elif num_quarter == 4: 
        print("значения координат точек в " + str(num_quarter) + " четверти  будут x > 0, y < 0") 

quarter = input()

# match quarter:
#     case "1":
#         print("x > 0, y > 0")
#     case "2":
#         print("x < 0, y > 0")
#     case "3":
#         print("x < 0, y < 0")
#     case "4":
#         print("x > 0, y < 0")
#     case _:
#         print("error")




