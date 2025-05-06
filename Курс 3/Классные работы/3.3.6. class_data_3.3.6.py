total_sum = 0
while True:
	try:
		user_input = input()
		if not user_input:
			break
		number = float(user_input)
		total_sum += number
	except ValueError:
		print("Некорректный ввод, попробуйте еще раз")
print(round(total_sum, 5))
