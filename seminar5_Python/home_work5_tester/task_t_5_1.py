# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

n =  int(input("введите количество слов: "))
if n < 0:
    print("The data is incorrect")
    exit()

liters3 = "бва"
import random
def list10(text): # делаем рандомное ['вба']
                    # из "бва"
    words = text.split()
    for i, word in enumerate(map(list, words)):
        random.shuffle(word)
        words[i] = ''.join(word)
    return words
a1 = list10(liters3)
# print(a1)   #рандомное ['вба']
 

def temp_list(text, num):
    all_list10 = []
    for i in range(num):                
        all_list10.append(*list10(text))
    return all_list10
 #['ваб', 'бав', 'бва', 'ваб', 'вба', 'ваб', 'абв', 'абв']
f2 = temp_list(liters3, n)

# exit()

def filtr_list(op):
    finish_list = []
    out_word = input("введите буквосочетание, слова с которым хотите исключить: ")  #абв
    for el in op:
        if out_word != el:
            finish_list.append(el)
    return finish_list
f3 = filtr_list(f2)

print(" ".join(f2))    
print(" ".join(f3))

# Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  Решение из парраллельной группы
# def main():
#     txt = 'ansабвdfk afdhiаБвauh asdhfia fisadpof adfuабвh afai iqaqfqif afhiaf fad'
#     print(txt)
#     txt = ' '.join(list(filter(lambda element: 'абв' not in element.lower(), txt.split())))
#     print(txt)
# if __name__ == "__main__":
#     main()



