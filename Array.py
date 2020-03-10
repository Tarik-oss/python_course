from random import randint
random_numbers = []
for x in range(0, 20):
    i = randint(1, 100)
    if x % 2 == 1:
        i = -i
    random_numbers.append(i)
    
all_try = 5
guess = 0
not_guess = 0

while all_try > 0:
    number = int(input('Please enter the number: '))
    equal = random_numbers.count(number)
    
    if number in random_numbers:
        print('You winner. You can guess a number.')
        print('{0} is repeats {1}'.format(number, equal))
        guess += 1
        all_try -= 1
        continue
    if number not in random_numbers:
        print('Sorry, you not guess. Lucky another time.')
        print('{0} is repeats {1}'.format(number, equal))
        not_guess += 1
        all_try -= 1
        continue

print()
print('Random array {0}'.format(random_numbers))
print('Guess {0} no guess {1}'.format(guess, not_guess))
print()
