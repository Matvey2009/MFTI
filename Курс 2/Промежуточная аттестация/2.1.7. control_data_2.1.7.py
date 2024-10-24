def how_many_times(j):
	a = ""
	for i in j:
		a+=i.lower()
	t = min(a.count("p"), a.count("y"), a.count("t"), a.count("h"), a.count("o"), a.count("n"))
	return t
