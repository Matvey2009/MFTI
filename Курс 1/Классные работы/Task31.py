x = int(input())
y = int(input())
z = int(input())
s = 0
while x >= y:
	x -= y
	x += z
	s += 1
print(s)
