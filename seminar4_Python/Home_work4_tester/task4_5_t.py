
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






f1 = open("t_file1.txt", "r") 

f1 = open("t_file1.txt", "r")
my_str1 = f1.read()
my_str1 = my_str1.replace(" = 0\n", "*x^0").replace("x ", "*x^1 ")
print(my_str1)
f1.close() 
 

f2 = open("t_file2.txt", "r")
my_str2 = f2.read()
my_str2 = my_str2.replace(" = 0\n", "*x^0").replace("x ", "*x^1 ")
print(my_str2)
f2.close()  

# сумма многочленов в предыдущей задаче, не доделала с файлами
# и так далее..
   