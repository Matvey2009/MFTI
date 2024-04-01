n = int(input())
b = 0
if n%4==0 and n%100!=0:
	print(True)
	b = 1
if n%400==0:
	print(True)
	b = 1
if b == 0:
	print(False)
