n = s = 1
while n!=0:
	n = int(input())
	if n == 0:
		break
	if str(n)[-1] == "2" and n % 4 == 0:
		s+=1
print(s-1)
