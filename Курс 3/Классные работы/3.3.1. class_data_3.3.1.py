file = input()
with open(file, 'r') as f:
	for i in range(8):
		print(f.readline(), end='')
