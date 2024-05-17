#Импортируем библиотеки
from bs4 import BeautifulSoup
import requests

#Создаём файл для записи данных
file = open("2.Оценки.txt", "w")

#Берём ссылку веб-странички для парсинга
url = 'https://edu.rk.gov.ru/journal-student-grades-action/u.3157'

#Делаем запрос сайту
res = requests.get(url)

#Проверяем доступность ссылки
if res.status_code == 200:
	#Извлекаем данные из электронного журнала
	soup = BeautifulSoup(res.text,'html.parser')

	#Берём все нужные оценки с нужными тегами
	marks = soup.findAll('mark', class_='cell_data')
	
	#Берём название предмета
	names = soup.findAll('name', class_='cell_data')

	#Извлекаем данные и записываем их в файл с оценками
	for data in marks:
		#Отделяем количество пропусков от общей статистики оценок
		if data == "&nbsp":
			file.write("Н")
		else:
			file.write(str(name) +  " " + str(data) +  " " + "\n")
else:
	#Выводим код об ошибки в случаи проблемы загрузки страницы
    print("Ошибка при получении страницы. Статус код:", response.status_code)
