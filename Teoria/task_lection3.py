# f = open("file_lection3.txt", "a") 
# str_nums = "1 2 3 5 8 15 23 38"
# f.write(str_nums) # записала строку с числами в файл
# f.close() 
f = open("file_lection3.txt", "r")
string = f.read()#1 2 3 5 8 15 23 38
f.close() 

char_list = string.split()# ['1', '2', '3', '5', '8', '15', '23', '38']
# for c in string: # идем по строке
#     char_list.append(int(c)) 
list_nums = [int(num) for num in char_list]  #[1, 2, 3, 5, 8, 15, 23, 38]
def f1(x):
    return x**2 #lambda x: x**2
list_tuples = [(int(num),f1(num)) for num in list_nums if num%2 == 0] #[(2, 4), (8, 64), (38, 1444)]
  



# # ******************************   2 способ **********************************************************************
def select(f, col):
    return [f(x) for x in col]
def where(f,col):
    return[x for x in col if f(x)]

char_list = ['1', '2', '3', '5', '8', '15', '23', '38']

res = select(int, char_list) #[1, 2, 3, 5, 8, 15, 23, 38]
res = where(lambda x: not x % 2, res)#[2, 8, 38]
res = select(lambda x:(x, x**2), res)#[(2, 4), (8, 64), (38, 1444)]



# # ******************************   3 способ **********************************************************************



char_list = ['1', '2', '3', '5', '8', '15', '23', '38']

res = map(int, char_list)   #[1, 2, 3, 5, 8, 15, 23, 38]
res = filter(lambda x: not x % 2, res)  #[2, 8, 38]
res = list(map(lambda x:(x, x**2), res))  #[(2, 4), (8, 64), (38, 1444)]