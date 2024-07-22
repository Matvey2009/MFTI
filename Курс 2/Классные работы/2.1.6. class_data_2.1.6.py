n, a, b, g, c = input().lower(), "ауоиэыяюеё", "бвгджзйклмнпрстфхцчшщ", 0, 0
for i in n:
	if i in a:
		g+=1
	elif i in b:
		c+=1
print(g, c)
