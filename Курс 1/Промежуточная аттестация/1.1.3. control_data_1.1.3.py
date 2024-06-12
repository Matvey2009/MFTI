n = int(input())
if n < 0 or n > 100:
	print('Недопустимый диапазон баллов')
elif n < 30:
	print(2)
elif n <= 60:
	print(3)
elif n <= 80:
	print(4)
elif n <= 100:
	print(5)
