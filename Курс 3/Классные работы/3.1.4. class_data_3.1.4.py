def generate_set(numbers):
	result = set()
	for num in numbers:
		string = str(num)
		count = numbers.count(num)
		for i in range(1, count + 1):
			result.add(string * i)
	return result
