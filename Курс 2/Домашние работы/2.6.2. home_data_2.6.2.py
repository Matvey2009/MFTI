def double_vowels(a):
	return "".join(list(map(lambda x: x*2 if x.lower() in ["а","у","о","и","э","ы","я","ю","е","ё","a","e","i","o","u","y"] else x, a)))
