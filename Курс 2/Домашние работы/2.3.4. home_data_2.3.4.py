def extract_numbers(text):
	arr = []
	temp = ""
	for i in text:
		if i.isdigit():
			temp+=i
		elif temp.isdigit():
			arr.append(int(temp))
			temp = ""
	return arr
