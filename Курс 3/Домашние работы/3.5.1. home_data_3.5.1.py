import numpy as np
fil, res, n = input(), 0, []
with open(fil, encoding="utf8") as filtemp:
	for i in filtemp:
		res = i.split()
		n.append(int(res[1]))
print(int(np.median(n)))

