# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input()
sum = 0
power = len(num) - 2
num = float(num)
num *= int(10 ** power)
while num:
    sum += int(num % 10)
    num //= 10
print(int(sum))    
