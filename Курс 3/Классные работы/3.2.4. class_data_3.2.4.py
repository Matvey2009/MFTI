def merge_dict(dict1, dict2):
	merge_dict = dict1.copy()
	for key, value in dict2.items():
		if key in merge_dict:
			merge_dict[key] += value
		else:
			merge_dict[key] = value
	sorted_dict = dict(sorted(merge_dict.items()))
	return sorted_dict
