__author__ = 'Khrishan'
__title__ = 'List Challenge'

# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.

menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage', 'bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

for meal in menu:
    if not 'spam' in meal:
        for item in meal:
            print(item)