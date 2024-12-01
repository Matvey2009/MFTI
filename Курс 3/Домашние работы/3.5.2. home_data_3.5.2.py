def my_mode(*arr):
	arr = list(arr)
	res = list()
	m=1
	t=len(arr)
	for i in arr:
		t = min(t, arr.count(i))
		if arr.count(i) > 1 and i not in res:
			if arr.count(i) == m:
				res.append(i)
			elif arr.count(i) > m:
				res = [i]
				m = arr.count(i)
	res.sort()
	if len(res) == 0 or t == m:
		return None
	elif len(res) == 1:
		return res[0]
	else:
		return tuple(res)
