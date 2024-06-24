s = input()
while '(' in s or ')' in s:
	left = s.rfind('(')
	right = s.find(')', left)
	s = s.replace(s[left:right + 1], '')
print(s)
