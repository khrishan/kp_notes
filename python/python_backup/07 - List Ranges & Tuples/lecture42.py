__author__ = 'Khrishan'
__title__ = 'Understanding Iterators'

# string = '1234567890'

# for char in string:
#     print(char)

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, when n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

items = [1, 2, 3, 4, 5, 6]
iterator = iter(items)

for i in range(0, len(items)):
    print(next(iterator))

# Instructor Code
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# iterator = iter(days)

# for i in range(0, len(items)):
#     print(next(iterator))
