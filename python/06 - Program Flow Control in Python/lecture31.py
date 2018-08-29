__author__ = 'Khrishan'
__title__ = 'Extended For Loops'

number = '9,223,372,036,854,775,807'
cleaned_number = ''

for char in number:
    if char in '0123456789':
        cleaned_number = cleaned_number + char

print('The new number is : {}'.format(cleaned_number))

for state in ['not pinin\'', 'no more', 'a stiff', 'bereft of life']:
    print('This parrot is {}'.format(state))

# This method put a step in as an extra parameter
for i in range(0, 100, 5):
    print('i is {}'.format(i))

for i in range(1,13):
    for j in range(1,13):
        print('{1} times {0} is {2}'.format(i, j, i*j))
    print('==================')