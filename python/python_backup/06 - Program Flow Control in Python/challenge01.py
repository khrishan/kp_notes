__author__ = 'Khrishan'
__title__ = 'Challenge #1 : If Then Else'

# The Challenge

# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right ago to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are , welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input('Please enter your name : ')
age = int(input('How old are you, {}?: '.format(name)))

if(18 <= age <= 30):
    print('You qualify! Welcome to the holiday!')
else:
    print('You do not qualify. I\'m sorry :(')