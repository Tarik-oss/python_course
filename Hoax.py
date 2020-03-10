# import modul random with function choice
# import modul time with function sleep
from random import choice
from time import sleep

# creat function with list of the players

def list_players(*args):
    return args

# creat function that choose the random players

def choose_player():
     name_of_player = list_players('Taras', 'Andriy', 'Vlad', 'Liosha', 'Nazar', 'Valentin')
     selected_player = choice(name_of_player)
     return selected_player

#creat function that output the winner to the screen

def Output():
    winner = choose_player()
    while True:
        sleep(1)
        break
    print('Hello everyone. Today we will know who is winner today! \n')
    while True:
        sleep(1)
        break
    print('Drum roll!!!! \n')
    for second in range(1, 6):
        print('\033[1m {}'.format('Bell '), second)
        sleep(1)
    print('\n Our winner is' + '\033[32m\033[1m {0}'.format(winner))

Output()
