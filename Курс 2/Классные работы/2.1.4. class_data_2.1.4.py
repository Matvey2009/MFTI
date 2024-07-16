a = input()
x1, x2 = 0, len(a)
for i in range(len(a)):
	if a[i] == "(":
		x1 = i
	elif a[i] == ")":
		x2 = i
print(a[:x1] + a[x2+1:])
