def final_price(*prices:float, discount:int = 1):
	return [i - i * discount / 100 for i in prices]
