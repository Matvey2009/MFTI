import numpy as np
def extract_var(f, prod):
	res = list()
	with open(f, encoding="utf8") as fil:
		for i in fil:
			if i.split(",")[1] == prod:
				res.append(int(i.split(",")[2]))
	return int(np.var(res))
