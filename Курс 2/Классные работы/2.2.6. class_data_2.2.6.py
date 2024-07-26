arr = list(map(int, input().split()))
tmp = list(map(int, input().split()))
for i in tmp:
	arr.append(i)
for i in range(len(arr)):
	for j in range(i, len(arr)):
		if arr[i] > arr[j]:
			arr[i], arr[j] = arr[j], arr[i]
print(arr)
