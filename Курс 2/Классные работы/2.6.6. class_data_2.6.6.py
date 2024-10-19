def long_livers(a, b):
	arr = []
	for i in zip(a, b):
		if i[0] >= 90:
			arr.append((i[0], i[1]))
	return arr
