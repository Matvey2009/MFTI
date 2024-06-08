col = 0
fin = ""
arr = ["а", "у", "о", "и", "э", "ы", "я", "ю", "ё", "е"]
while col < 30:
	n = input()
	if str(n[0]) not in arr:
		col += len(n) + 1
		fin += (" " + n)
print(fin)
