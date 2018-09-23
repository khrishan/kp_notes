__author__ = 'Khrishan'
__title__ = 'More Lists'

list1 = []
list2 = list()

print('List 1 : {}'.format(list1))
print('List 2 : {}'.format(list2))

if list1 == list2:
    print('The lists are equal!')

print(list('The lists are equal!'))

even = [2, 4, 6, 8]
another_even = even # another_even = list(even) <- this is how to fix the issue!
another_even.sort(reverse=True) # This sorts both even and another_even (as another_even is a reference to even)

print(even)