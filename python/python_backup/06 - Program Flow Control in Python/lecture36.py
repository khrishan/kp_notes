__author__ = 'Khrishan'
__title__ = 'While Loops'

import random

# for i in range(10):
#     print('i is now {}'.format(i))

# print('')

# i = 0
# while i < 10:
#     print('i is now {}'.format(i))
#     i += 1

# exits = ['north', 'south']

# chosen_exit = ''

# while chosen_exit not in exits:
#     chosen_exit = input('Please choose a direction : ')

#     if(chosen_exit == 'quit'):
#         print('Game Over!')
#         break
# else:
#     print('Aren\'t you glad you got out of there!')

highest = 10
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}'.format(highest))

while True:
    guess = input()
    if guess == '':
        print('You haven\'t entered anything!\nPlease enter a number : ')
        continue
    else:
        guess = int(guess)
    if guess == 0:
        break
        print('Please enter a value!')
    elif guess != answer:
        if guess < answer:
            print('Wrong! Please Guess Higher!')
        else:
            print('Wrong! Please Guess Lower!')
    else:
        print('BINGO! You guessed correctly!')
        break