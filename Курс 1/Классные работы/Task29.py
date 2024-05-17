n = int(input())
k = ""
for i in range(1, n+2):
	for j in range(1, i):
		k += str(j) + " " 
print(k)
