def filter_unique_words(arr):
	arr = list(arr.split())
	k = []
	def s(a):
		if arr.count(a) == 1:
			return a
	return list(filter(s , arr))
