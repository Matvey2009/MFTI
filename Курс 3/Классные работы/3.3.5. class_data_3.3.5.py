def get_top_url(logfile):
	with open(logfile, 'r') as f:
		lines = f.readlines()
		urls = [line.split(' | ')[2] for line in lines]
		top_url = max(set(urls), key = urls.count)
		return top_url.split()[1]
