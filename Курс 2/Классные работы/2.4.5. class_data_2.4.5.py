def delete_from_tuple(x, d):
	arr = []
	for i in x:
		if i != d:
			arr.append(i)
	return tuple(arr)
