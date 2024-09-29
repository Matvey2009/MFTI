def after_sum(*x):
	t = 0
	for i in range(len(x)):
		if x[i] < 0:
			t += 1
		if t == 2:
			c = i
			break
	t = 0
	for i in range(c+1, len(x)):
		if x[i] % 2 == 0:
			t+=x[i]
	return t
