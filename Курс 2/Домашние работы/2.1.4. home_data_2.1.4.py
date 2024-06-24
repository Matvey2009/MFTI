n, clone = input(), ""
for i in range(len(n)):
	clone+=n[i] 
	n += "K"
	if (n[i] == "," or n[i] == ".") and n[i+1] != " ":
		n = n[:-1]
		clone+=" "
print(clone[:-1])
