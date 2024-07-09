def only_digits(a):
	return list(filter(  lambda x: x if x.isdigit() else 0, a))
