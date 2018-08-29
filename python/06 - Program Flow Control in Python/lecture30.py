__author__ = 'Khrishan'
__title__ = 'For Loops'

# Last number is not included

for i in range(1,20):  
    print('i is now {}'.format(i))

number = '9,223,372,036,854,775,807'

for i in range(0, len(number)):
    print(number[i])

number = '9,223,372,036,854,775,807'

# Default is for every print statement that you add a new line (\n)
# To change that put a comma (,), then put end='' to remove it

cleaned_number = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleaned_number = cleaned_number + number[i]
        #print(number[i], end='')

new_number = int(cleaned_number)

print('The number is {}'.format(new_number))