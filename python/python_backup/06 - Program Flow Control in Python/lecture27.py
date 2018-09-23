__author__ = 'Khrishan'

# IF Program Flow

# name = input('Please enter your name: ')
# age = int(input('How old are you, {0}?: '.format(name)))

# print(age)

# if age >= 18:
#     print('You are old enough to drink!')
#     print('Please spend all your money here and get plastered!')
# else:
#     print('Please come back in {0} years time.'.format(18 - age))

print('Please guess a number between 1 and 10: ')
guess = int(input())

# if guess < 5:
#     print('Please guess higher! : ')
#     guess = int(input)
#     if(guess == 5):
#         print("Well Done you guessed it!")
#     else:
#         print('Sorry, you have not guessed correctly.')
# elif guess > 5:
#     print('Please guess lower! : ')
#     guess = int(input())
#     if(guess == 5):
#         print("Well Done you guessed it!")
#     else:
#         print('Sorry, you have not guessed correctly.')
# else:
#     print('Correct! You got it first time!')

# You can Simplify the above code.

if guess != 5:
    if guess < 5:
        print('Please guess higher! : ')
    else: # Guess must be greater than 5
        print('Please guess lower! : ')

    guess = int(input())
    if(guess == 5):
        print("Well Done, you guessed it!")
    else:
        print('Sorry, you have not guessed correctly.')
else:
    print('You got it first time!')

# All Operators == , != <= >= < >