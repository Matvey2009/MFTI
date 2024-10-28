def winners(a, b, c):
	result = ''
	for i in list(sorted(set(a.split()).intersection(set(b.split()), set(c.split())))):
		result += " " + i
	if result:
		return result[1:]
	else:
		return "Все три задачи никто не решил"
