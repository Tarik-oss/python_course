# Ліпше стилізувати словники наступним чином
# це дозволить ліпше сприймати інформацію
names = {
    'Taras':'Taras Palagnuk',
    'Nazar':'Nazar Gardienko',
    'Andrey':'Andrey Myzik',
    'Vlad':'Vlad Kulcziskiy',
    'Franc':'Franc Gaur'
}

# бажано старатися мінімізувати логічні вкладення і розбивати їх на блоки
# while можна застосувати для очікування введення даних
# пропоную вивести код наступним чином:
# за необхідності, користувач запустить програму ще раз

# 1 - виводимо список імен
# при цьому використання format це чудова ідея
for item in names.keys():
    print('Enter this name {0} for look their full names'.format(item))

# 2 - отримуємо ім"я користувача
print('For start enter key \'s\' and for enter key \'e\'')
name = input('Please enter the short name: ')

# 3 - шукаємо користувача та видаємо результат
if name in names:
    print('Full name {0}'.format(names[name]))
else:
    print('Hello strange. I do not familiar with you.')

value = True
while value:
    print('For start enter key \'s\' and for enter key \'e\'')
    #comand -> command
    comand = input('Enter key s for start')
    if comand == 's':
        name = input('Please enter the short name: ')
        if name in names:
            print('Full name {0}'.format(names[name]))
        else:
            print('Hello strange. I do not familiar with you.')
    elif comand == 'e':
        print('End of the programe')
        value = False
