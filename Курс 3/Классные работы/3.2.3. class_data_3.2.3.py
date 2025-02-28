def check_alex(names, grades):
	names_list = names.split()
	grades_list = grades.split()
	grades_dict = {}

	for i in range(len(names_list)):
		name = names_list[i]
		grade = int(grades_list[i])
		grades_dict[name] = grade

	if 'Саша' not in grades_dict:
		return "Саша не найден"
	elif grades_dict['Саша'] > 3:
		return "Зачтено"
	else:
		return "Отчислен"
