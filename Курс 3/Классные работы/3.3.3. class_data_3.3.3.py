def swap_kg(filename):
	with open(filename, 'r') as f:
		text = f.read()

	new_text = text.replace('kg', 'кг')
	with open('kg_replaced.txt', 'w') as f:
		f.write(new_text)
