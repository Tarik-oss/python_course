from random import randint

# зі створенням масиву з випадковими числами все чудово
random_numbers = []
for x in range(0, 20):
    i = randint(1, 100)
    if x % 2 == 1:
        i = -i
    random_numbers.append(i)

# непоганою ідеєю було б виводити масив, адже нам треба перевірити чи кожне друге число є від"ємним
print(random_numbers)

all_try = 5
guess = 0
not_guess = 0

# бажано додати перевірку на коректність значення
# наприклад через assert
while all_try > 0:
    number = int(input('Please enter the number: '))
    equal = random_numbers.count(number)
    
    if number in random_numbers:
        print('You winner. You can guess a number.')
        print('{0} is repeats {1}'.format(number, equal))
        guess += 1
        all_try -= 1
        # в continue немає сенсу, адже друга умова не виконається, 
        # адже вона є протилежною до першої
        continue
    # if можна поміняти на else, тоді код буде виконуватися тільки тоді,
    #  коли не виконується перша умова
    if number not in random_numbers:
        print('Sorry, you not guess. Lucky another time.')
        print('{0} is repeats {1}'.format(number, equal))
        not_guess += 1
        all_try -= 1
        # тут continue не має сенсу, адже це кінець ітерації
        continue

print()
print('Random array {0}'.format(random_numbers))
print('Guess {0} no guess {1}'.format(guess, not_guess))
print()
