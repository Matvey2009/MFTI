input_string = input()
with open('out.txt', 'w') as f:
	with open('in.txt', 'r') as file_in:
		file_content = file_in.read()
	f.write(input_string + "\n" + file_content)
