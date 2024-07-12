def calculate_average_grades(arr, user):
	res = []
	for i in zip(arr, user):
		res.append((i[1], int(sum(i[0])/len(i[0]))))
	return res
