#6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z)) 
#print("x y z") 
#for x in range(2): 
  #  for y in range(2): 
   #     for z in range(2): 
    #        if not (x == z or x <= y and z): 
     #           print(x, y, z) 
 
#2. Напишите программу для проверки ложности утверждения 
#(W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат. 
print("x y z w") 
for x in range(2): 
    for y in range(2): 
        for z in range(2): 
            for w in range(2): 
                if not ((w and z) or not y or ((not x) == (not w))): 
                    print( x, y, z, w) 