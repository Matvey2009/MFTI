def set_grade(d1, d2):
	result = {}
	for sd in d1:
		n = round((sum(map(int, d1[sd].split()))/(len(d1[sd].split())))+0.000000000000001)
		for key, value in d2.items():
			if n in value:
				result[sd] = key
	return result
