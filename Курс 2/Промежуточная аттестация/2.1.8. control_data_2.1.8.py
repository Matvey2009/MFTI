def t9(a, b):
	res = []
	arr = [" ", ".,-", "абвг", "дежз", "ийкл", "мноп", "рсту", "фхцч", "шщъы", "ьэюя"]
	for i in a.split():
		t = 0
		for j in range(min(len(str(b)), len(i))):
			if i[j].lower() in arr[int(str(b)[j])]:
				t += 1
		if t == len(str(b)):
			res.append(i)
	return " ".join(res)
