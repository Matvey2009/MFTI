n = int(input())
if n < 0:
	print("Ошибка. Число отрицательное")
else:
	s = 0
	for i in range(n):
		if i % 2 == 1:
			s+=i
	print(s)
