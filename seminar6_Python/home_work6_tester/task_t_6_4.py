# 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
#  возвращает словарь, ключи — первые буквы фамилий, значения — словари,
# реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# out

{
 'С': {'А': ['Анна Савельева', 'Антон Серов'], 'И': ['Иван Сергеев', 'Инна Серова']},
 'А': {'Б': ['Борис Аркадьев'], 'П': ['Павел Анисимов', 'Петр Алексеев']},
 'И': {'И': ['Илья Иванов']}, 
 'В': {'Ю': ['Юнона Ветрякова']}
             }


names_sername = "Иван Сергеев", "Инна Серова", "Петр Алексеев",
"Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
"Борис Аркадьев", "Антон Серов", "Павел Анисимов"

# n_s = "Иван Сергеев"                              
#                                                      
# 
#                    *******************************#   не доделано  *************************

# liter = И

names_dict_set = dict()
names_dict_list= []
for j, n_s in enumerate(names_sername):
    for i, liter in enumerate(n_s, 1):
        if liter.istitle():
            key_first_letter = liter
    names_dict_list.append(n_s[j])            
    names_dict_set[key_first_letter] = names_dict_set.setdefault(key_first_letter, set()) + [names_dict_list]

            
print()
print(names_dict_set)

                                                    
