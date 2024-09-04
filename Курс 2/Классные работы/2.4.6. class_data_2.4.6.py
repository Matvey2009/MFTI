def telephone(x):
	if len(x[2:]) == 10 and x[2:].isdigit() and x[:2] == "+7":
		return True
	else:
		 return False

