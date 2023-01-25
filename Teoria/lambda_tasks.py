


# Анонимные, lambda функции

def sum(x):      
 return x+10       #sum = lambda x: x+10

def sum1(x):       #sum1 = lambda x: x+22
 return x+22

def sum3(x):       #sum3 = lambda x: x + 242
 return x+242

def mult(x):
 return x**2       #mult = lambda x: x**2

def mult2(x):      # mult2 = lambda x: x**3
 return x**3


def mult4(x):
 return x**5           #mult4 = lambda x: x**5
 
print(sum3(mult2(2))) #250
print(sum(mult(2)))   #14
print(sum1(mult2(2))) #30







