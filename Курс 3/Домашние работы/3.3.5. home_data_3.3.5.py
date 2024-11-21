def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False
leap_years = []
while True:
    try:
        user_input = input()
        if user_input == '':
            break
        
        year = int(user_input)
        
        if year < 1900 or year > 2024:
            print("Некорректный ввод, попробуйте еще раз")
        else:
            if is_leap_year(year):
                leap_years.append(year)
    except ValueError:
        print("Некорректный ввод, попробуйте еще раз")
print(leap_years)
