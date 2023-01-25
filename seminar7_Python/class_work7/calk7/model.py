# инициализация начальных значений
# def calc_data():

a = 0
b = 0

def init_a(number: int):
   global a
   a = number

def init_b(number: int):
   global b
   b = number

def get_a():
   global a
   return a

def get_b():
   global b
   return b

