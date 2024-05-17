n = int(input())
x1 = 0
x2 = 1
for i in range(1, n+1):
	x = x1+x2
	x2 = x1
	x1 = x
print(x)
