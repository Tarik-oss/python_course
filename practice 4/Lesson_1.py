# Все що було закоментоване я переніс в файл Lesson_1 copy.py
# За умовою користувач може ввести будь-які відсотки
# однак, це не є проблемою


# опис функцій є класною звичкою
# ось приблизний приклад
""" Should retrieve interest rate 
    Args:
        *args (float[]): List of available rate
    Returns:
        float: selected rate
"""
def Percent(*args):
    for number, percent in enumerate(args):
        print('Please choose the number {0} of the percent {1}'.format(number, percent))
    
    # Гарна ідея використати try catch для перевірки коректності значення заданого користувачем
    try:
        # змінну а ліпше називати по її контексту
        # a -> rateIdx або rateIndex
        a = int(input('Enter please number: '))
        a -= 1
    except ValueError:
        return 'Wrong value. Please enter the number.'

    #else не має сенсу
    else:
        # в цьому випадку цикл не є доречним
        # також не коректно використовувати змінну і об"явлену в області циклу поза ним
        for i in range(0, len(args)):
            if a == i:
                return args[i]
        if a > i or a <= i:
            return 'Wrong value.'

        # код вище (29-33 стрічки) ліпше поміняти на:
        if a < 0 and a >= len(args):
            return 'Wrong value.'
        return args[a]

# див 6 стрічку
# value1 та value2 треба замінити на назви згідно контексту
def Exiting(value1, value2):
    # після коми ми зазвичай додаємо порожній символ, для ліпшої читабельності    
    # y -> interestRate
    y = Percent(0.05, 0.1 ,0.15, 0.20)

    # перевірки на коректність (54, 56, 64 стрічки) процентної ставки ліпше робити поза циклом
    # використовуючи їх у циклі, ми будемо здійснювати зайві операції
    # e -> year
    for e in range(0, value2):
        
        if y == str(y):
            print(y)
        elif y == float(y):
            # ця зміння треба для прикладу з print, щоб ми знали річний прибуток
            #profit = value1 * y
            value1 = value1 * y + value1
            # Ліпше виводити наступний коментар:
            # Однак, гарна ідея використовувати форматування чисел з крапкою через format
            #print("{0} year, summ: {1:.2f}, profit per year: {2:.2f}".format(e + 1, value1, profit))
            print('Suma of the deposit for 12 mounth = {0:.2f}'.format(value1))
        elif y == None:
            print(y)

# також користувач має бути в змозі вказати тривалість депозиту та суму
Exiting(500, 12)