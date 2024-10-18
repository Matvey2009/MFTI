def compare_test_results(a, b, c):
	arr = []
	for i in zip(a, b, c):
		if i[0] > 60 and i[1] > 60:
			arr.append((i[2], "Да"))
		else:
			arr.append((i[2], "Нет"))
	return arr
