c, i = list(map(int, input().split())), 0
while i != len(c):
	if c[i] > 9:
		c.pop(i)
		i=i-1
	i=i+1
print(c)
