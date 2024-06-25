n = list(map(int, input().split()))
result = list()
for i in n:
	if i < 0 and i%2 == 0:
		result.append(i)
print(result)
