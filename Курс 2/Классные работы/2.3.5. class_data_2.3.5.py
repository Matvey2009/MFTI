def num_to_list(string:str, box:list):
	for i in string.split():
		box.append(int(i))
	return box
