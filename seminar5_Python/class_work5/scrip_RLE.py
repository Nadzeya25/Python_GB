#  encoding (RLE)
def RLE_encode(s):
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

# if __name__ == '__main__':
str1 = 'ffllllffrrrrrwwwwoo'
print(RLE_encode(str1))

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

# print(rle_decode(test_data))