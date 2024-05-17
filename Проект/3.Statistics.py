#Импортируем библиотеки
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

#Чтения файла с оценками
file = open("2.Оценки.txt", "r")

#Создание массивом для работы с ними в будущем
poradok = list()
marks = list()
array = list()
bio = list()
mat = list()
phi = list()

#Обработака данных файлов
for i in file:
	ocenka = int(i.split(' ')[1][0])
	urok = i.split(' ')[0]
	
	#Распределяю оценки по массивам
	if urok == "Биология":
		bio.append(ocenka)
	if urok == "Математика":
		mat.append(ocenka)
	if urok == "Физика":
		phi.append(ocenka)
		
#Вывод среднеарифметической по школьным предмет
print("Средняя оценка по Биологии:", round(sum(bio)/len(bio), 2))
print("Средняя оценка по Матиматике:", round(sum(mat)/len(mat), 2))
print("Средняя оценка по Физики:", round(sum(phi)/len(phi), 2))

#Добавляю мои оценки на график
plt.plot(bio)
plt.plot(mat)
plt.plot(phi)

#Отображаю график через библиотеку matplotlib.pyplot
plt.title('График оценок')
plt.xlabel('Балл')
plt.ylabel('Число оценок')
plt.show()


