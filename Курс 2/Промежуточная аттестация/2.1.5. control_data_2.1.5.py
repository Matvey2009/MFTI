def is_palindrome(a):
	k = ""
	for i in a:
		if i != " " and i.isalnum():
			k += i.lower()
	if k == k[::-1]:
		return True
	else:
		return False
