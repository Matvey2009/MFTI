n = input()
l = len(n)
while l > 0:
	print(n[:5])
	n=n[5:]
	l-=5
