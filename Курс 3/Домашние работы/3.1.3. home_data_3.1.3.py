def cat_names(a, b):
	result = ''
	for i in list(sorted(set(a) - set(b))):
		result += " " + i  
	return result[1:]
