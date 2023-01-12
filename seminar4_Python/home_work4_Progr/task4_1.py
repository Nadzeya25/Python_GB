# Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141
# d от 0.1 до 0.0000000001
import math
p = list(str(math.pi))
print(p)

def CalculatePi(roundVal):
    somepi = round(math.pi,roundVal)
    pi = str(somepi)
    someList = list(pi)
    return somepi
roundTo = input("Введите число, определяющее количество знаков дробной части числа π : ")
try:
    roundint = int(roundTo)
    print(CalculatePi(roundint))
except:
    print("вы ввели не число")


