__author__ = 'Khrishan'
__title__ = 'Understanding Ranges'

# print(range(100)) # not useful

# my_list = list(range(10))
# print(my_list)

# even = list(range(0, 10, 2)) # start value, end value, steps
# odd = list(range(1, 10, 2))

# print(even)
# print(odd)

# my_string = 'abcdefghijklmnopqrstuvwxyz'
# print(my_string.index('e'))
# print(my_string[4])

# small_decimals = range(0,10)
# print(small_decimals)

# print(small_decimals.index(3))

# odd = range(1, 10000, 2)
# print(odd)

# print(odd[195])

# sevens = range(7, 100000, 7)
# x = int(input('Please enter a value between 0 to 1,000,000 : '))

# if x in sevens:
#     print('{} is divisble by 7'.format(x))

# print(small_decimals)

# my_range = small_decimals[::2] # skip over every other one
# print(my_range)
# print(my_range.index(4))

decimals = range(0,100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print('=' * 40)