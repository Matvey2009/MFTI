def percent_ok(logfile):
	with open(logfile, 'r') as f:
		lines = f.readlines()
		counter = 0
		for line in lines:
			if int(line.split(' ')[-1]) == 200:
				counter += 1
		result = round(counter / len(lines) * 100, 1)
		return result 
