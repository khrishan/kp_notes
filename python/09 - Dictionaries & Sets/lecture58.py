__author__ = 'Khrishan'
__title__ = 'Sets'

# Two ways to create sets

# farm_animals = {'sheep', 'cow', 'hen'}
# print(farm_animals)

# wild_animals = set(['lion', 'tiger', 'panther', 'hare']) # can only use this if we want to create an empty set
# print(wild_animals)

# farm_animals.add('horse')
# wild_animals.add('horse')

# print(farm_animals)
# print(wild_animals)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares))
# print(len(even.union(squares)))

# print('-' * 40)

# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# #set a - set b removes items that are in set a from set b
# print(squares.difference(even))
# print(squares - even)

# print('-' * 40)

# X_update updates the set that it is being called upon

# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))

# # symmetric difference - opposite of intersection!

# print('symmetric even minus squares') 
# print(sorted(even.symmetric_difference(squares)))

# print('symmetric squares minus even')
# print(sorted(squares.symmetric_difference(even)))

# # removing something from a set that isn't there
# # would cause an error but discarding something
# # that isn't there does cause an error

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# # squares.remove(8) # this is the method that would cause an error!

# # why would you use remove if discard doesn't produce an error - it may be useful to produce an error!



# try:
#     squares.remove(8)
# except KeyError:
#     print('The item 8 is not a member of the set!')


# #is subset if all members are contained

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(sorted(squares))

if squares.issubset(even):
    print('squares is a subset of even')

if even.issuperset(squares):
    print('even is a superset of even')

# frozenset is an immutable set - once created it cannot be changed - 

even = frozenset(0, 100, 2)
print(even)