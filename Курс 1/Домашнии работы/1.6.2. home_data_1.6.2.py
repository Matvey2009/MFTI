n = 1
arr = list()
while n != 0:
	n = int(input())
	if n not in arr:
		arr.append(n)
arr.sort()
print(arr[len(arr)-2])
