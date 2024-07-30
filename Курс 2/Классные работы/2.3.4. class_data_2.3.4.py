def div(n:int):
	result = [1, n]
	for i in range(2, n // 2 + 1):
		if n % i == 0:
			result.append(i)
	return len(result)
