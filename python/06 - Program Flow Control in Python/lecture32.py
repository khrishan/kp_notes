__author__ = 'Khrishan'
__title__ = 'Undderstanding Continue, Break and Else'

shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

for item in shopping_list:
    if item is 'spam':
        continue
    print('Buy {}'.format(item))

print('===========')

for item in shopping_list:
    if item is 'spam':
        break
    print('Buy {}'.format(item))

meal = ['egg', 'bacon', 'beans', 'sausages']

nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else: 
    print('I\'ll have a plate of that then! Please :)')

# else can be put with the for as well as the if

if nasty_food_item == 'spam':
    print('Can\'t I have anything without spam in it')