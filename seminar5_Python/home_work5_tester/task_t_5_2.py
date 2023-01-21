# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q
file1 = input('Enter the name of the file with the text:')
file2 = input('Enter the file name to record:')
text1 = 'aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa\nvbbwwPPuuuTTYyWWQQ\n'

with open(file1, 'w') as w_start_text1:  #записываем данные из задания в файл1
	w_start_text1.writelines(text1)

#  encoding (RLE)
def rle_encode(s):
	encoding = ""
	i = 0
	while i < len(s):
		# подсчет вхождений символа по индексу i
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		# добавляем текущий символ и его количество к результату
		encoding += str(count) + s[i]
		i = i + 1
	return encoding

#записываем кодированный текст  в файл2
with open(file2, 'w') as finish_text:
	finish_text.writelines(rle_encode(text1))


# декодируем обратно
def rle_decode(data):
	decode = '' # буква
	count = ''  # число
	for char in data:
		if char.isdigit():  # Если символ числовой
			count += char     #добавим его к счетчику
		else:
			# Otherwise we've seen a non-numerical 
			# # character and need to expand it for # the decoding 
			decode += char * int(count)
			count = '' 
	return decode

# дописываем ранее кодированный, а потом декодированный текст в файл2
with open(file2, 'a') as finish_text:
	finish_text.writelines(rle_decode(rle_encode(text1)))
