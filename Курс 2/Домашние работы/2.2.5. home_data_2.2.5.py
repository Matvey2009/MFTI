n = list(map(int, input().split()))
n.append("Чебурек")
maxi = t = 0
for i in range(len(n)):
	if n[i] == 0:
		t+=1
	else:
		maxi, t = max(maxi, t), 0
print(maxi)
