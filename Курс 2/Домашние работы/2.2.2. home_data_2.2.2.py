n = list(map(int, input().split()))
b1, b2 = n[0:len(n)//2], list()
b1.reverse()
for i in range(len(n)//2, len(n)):
	b2.append(n[i])
b2.reverse()
for i in range(len(n)//2):
	b1.append(b2[i])
print(b1)

