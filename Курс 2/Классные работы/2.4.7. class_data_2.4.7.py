def bubble_sort(x):
	for i in range(len(x)):
		for j in range(i, len(x)):
			if x[i] > x[j]:
				x[i], x[j] = x[j], x[i]
	return x

