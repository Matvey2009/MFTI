def series(n):
	s = 2
	for i in range(2, n):
		s = s + i * (i + 1)
	return s
