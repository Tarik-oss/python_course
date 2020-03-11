# необхідно явно додати модуль календаря, по замовчуванню в нас немає цього модуля 
# і для запуску коду, мені треба його скачати руками
# треба щоб код запускався одразу без додаткових маніпуляцій

# import modul calendar
import calendar

#creat the object of calendar
obj = calendar.Calendar()

# також, є дещо не коректним отримання даних від користувача в наступному форматі, адже в завданні
# було зазначено, що дата має передаватися як стрічка dd-mm-yyyy 
# year, month, date = int(input('Enter the year than month than date: ').split())
while True:
    year = input('Year: ')
    month = input('Month: ')
    date = input('Date: ')
    #cheak mistake of the input
    # mistake of the lenght

    # це гарна ідея перевіряти на коректність коду
    # в ідеалі варто було б винести отримання значень в окрему функцію, 
    # це дозволило б спростити вкладеність і полегшити розуміння коду
    if len(year) > 4 or len(month) > 2 or len(date) > 2:
        print('Very long value. Please enter the short value')
    elif year.isdecimal() == True and month.isdecimal() == True and date.isdecimal() == True:

        year = int(year)
        month = int(month)
        date = int(date)
        # mistake of the month range 
        if month <= 0 or month >= 13:
            print('Wrong month. Please enter the month from 1 to 12.')
            continue
        # mistake of the year range
        elif year < 1999 or year > 2100:
            print('Wrong year. Please enter the year from 2000 to 2099.')
            continue
        break
    #cheak mistake of the input information (must be integer)
    elif year.isdecimal() == False or month.isdecimal() == False or date.isdecimal():
        print('You enter the wrong key.')

# work cycle
for day in obj.itermonthdays2(year, month):
    # equal the date witt day index
    if date == day[0]:
        # if day is work
        # якщо ми використовуємо певну зміну з модуля багато разів, ліпше її отримати на пряму
        # Наприклад from calendar import day_name, month_name
        # Після можна буде використовувати їх на пряму як day_name[day[1]]

        # Також ліпше притримуватися правила 120 символів на стрічку
        # Це правило допомагає притримуватися чим більш простої логіки на один рядок
        # Та дозволяє уникнути горизонтального скролінгу
        if day[1] == 5 or day[1] == 6:
            print('{0} {1} {2} {3} This is weekend day.'.format(calendar.day_name[day[1]], day[0], calendar.month_name[month], year))
        # if is weekend
        elif day[1] > 0 and day[1] < 4:
            print('{0} {1} {2} {3} This is working day.'.format(calendar.day_name[day[1]], day[0], calendar.month_name[month], year))
    # elif date == day[0]:
    #     print('{0} do not have this date {1}'.format(calendar.month_name[month], date))
