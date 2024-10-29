def inf_mean(d, sd):
	if sd not in d:
		return "Ученик не найден"
	else:
		return round((sum(map(int, d[sd].split()))/(len(d[sd].split())))+0.000000000000001)
