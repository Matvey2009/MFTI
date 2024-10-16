def complex_filter(arr):
	def f(a):
		if a == 0:
			return '0'
		elif a % 4 == 0:
			return a
	return list(filter(f, arr))
