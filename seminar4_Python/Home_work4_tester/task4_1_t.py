# 1. Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

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