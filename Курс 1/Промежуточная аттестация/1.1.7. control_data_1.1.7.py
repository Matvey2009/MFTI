x = int(input())
p = int(input())
y = int(input())
v=0
while x < y:
	x += x/100*p
	x = int(x)
	v +=1
print(v)
