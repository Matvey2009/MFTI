def sum_range(start, end):
	start, end = min(start, end), max(start, end)
	return int((start + end)*(end - start+1)/2)
