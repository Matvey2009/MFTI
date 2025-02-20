d = {}
for i in input().split():
	d[i] = len(i)
d = dict(sorted(d.items()))
print(d)
