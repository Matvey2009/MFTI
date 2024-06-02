a = input()
b = input()
s = k = 0
for i in a:
	if i == b:
		s += 1
	elif i == "@":
		print("Недопустимый символ")
		k = 1
		break
if k == 0:
	print(s)
