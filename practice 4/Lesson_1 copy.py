# також користувач має бути в змозі вказати усі три параметри:
# тривалість депозиту, суму, відсоткову ставку

# press the key, but enter the sum
suma = int(input('Press the summa: '))
# Добре було б робити перевірки на коректність значення з підказкою що трапилося
# це можна робити як з if, так і через assert
percent = 0.05
time_of_deposite = 12

for i in range(0, time_of_deposite):
    suma = suma * percent + suma
    # також бажано виводити рік та річний прибуток
    # це дозволить ліпше розуміти користувачу доцільність укладання депозиту
    # гарна ідея використовувати форматування
    print('Suma {0:.2f}'.format(suma))
    
# також назви змінних згідно контексту
list1 = [5, 10, 15 ,20]

a = int(input('Enter number of the range: '))
for item in range(0, len(list1)):
    if a == item:
        print(list1[item])
      
# # якщо в нас список об"єктів, ліпше вказувати назву змінної у множині
# # name -> names
# # між елементами після коми мають бути пробіли
# name = ['Valentin','Nazar','Franc','Taras']
# for i in name:
#     print('Hello my dear {0}'.format(i))