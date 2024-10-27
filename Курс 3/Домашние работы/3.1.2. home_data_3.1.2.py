def yes_or_no(st):
	k, result = [], ""
	for i in st.split():
		if i not in k:
			k.append(i)
			result += " NO"
		else:
			result += " YES"
	return result[1:]
