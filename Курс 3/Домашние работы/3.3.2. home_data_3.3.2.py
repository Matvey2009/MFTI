files = input().split()
not_found_files = []
merged_content = ""
for file in files:
	try:
		with open(file, 'r') as f:
			merged_content += (f.read() + "\n")
	except FileNotFoundError:
		not_found_files.append(file)
merged_content = merged_content[:-1]
print(merged_content)
if not_found_files:
	print("Файлы не найдены:", ' '.join(not_found_files))
