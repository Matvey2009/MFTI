def make_grades(names, grades):
	names_list = names.split()
	grades_list = grades.split()
	grades_dict = {}
	for i in range(len(names_list)):
		name = names_list[i]
		grade = int(grades_list[i])
		grades_dict[name] = grade
	return grades_dict
