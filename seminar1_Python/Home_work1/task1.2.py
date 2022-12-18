#2. Напишите программу для проверки ложности утверждения 
#(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат. 
print("x y z w") 
for x in range(2): 
    for y in range(2): 
        for z in range(2): 
            for w in range(2): 
                if not ((w and z) or not y or ((not x) == (not w))): 
                    print( x, y, z, w) 

# Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# for x in [False, True]:
#     for y in [False, True]:
#         for z in [False, True]:
#             if (not x or y or z) != (not x or y or z):
#                 print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - False')
#                 break
# else:
#     print('Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - True')
