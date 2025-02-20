def consonants(st):
	st = st.lower()
	vg = "!?.,:;- "
	for i in vg:
		st = st.replace(i, "")
	g = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
	return sorted(set(st) - g)
