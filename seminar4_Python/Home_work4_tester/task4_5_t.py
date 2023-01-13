
# ** 5. Даны два файла, в каждом из которых находится запись многочленов.
#  Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!



# сумма многочленов в предыдущей задаче, не доделала с файлами

f = open("file1.txt", "r") 
for line in f:
        print(line.replace("\n", ""))

f = open(r"C:\Users\lustr\OneDrive\Документы\Python_GB\seminar4_Python\home_work4_Progr\file2.txt", "r") 
for line2 in f:
        print(line2.replace("\n", ""))    