__author__ = 'Khrishan'
__title__ = 'Python Dictionaries'

fruit = {'orange': 'a sweet orange citrus fruit',
         'apple' : 'good for making cider',
         'lemon' : 'a sour, yellow citrus fruit',
         'grape' : 'a small, sweer fruit growing in bunches',
         'lime'  : 'a sour , green citrus fruit',
         'apple' : 'round and crunchy',
        }

fruit['pear'] = 'An odd shaped apple'
fruit['lime'] = 'great with tequilla'

print(fruit['apple'])

# can't use mutable objects as keys, can only use immutable object (so can therefore use a tuple)

# How to remove items from a dictionary
print(fruit)
del fruit['lemon'] # del fruit removes the whole reference
# fruit.clear removes all the references in the fruit dictionary
print(fruit)

# while True:
#     dict_key = input('Please enter a fruit : ')
#     if dict_key == 'quit':
#         break
#     description = fruit.get(dict_key, 'We don\'t have a {}'.format(dict_key))
#     print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print('We don\'t have a {}'.format(dict_key))
    

# bike = {'make'       :'Honda',
#         'model'      :'250 Dream',
#         'colour'     :'red',
#         'engine_size': 250 
#        }

# print(bike['make'])
# print(bike['model'])

# How to get an ordered list of keys from a dictionary
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for f in ordered_keys:
#     print(f + ' - ' + fruit[f])

# # This is less efficient
# for val in fruit.values():
#     print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit['tomato'] = 'not nice with ice cream'
# print(fruit_keys)

# items object
# print(fruit)
# print(fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)

# for snack in f_tuple:
#     item, description = snack
#     print(item + ' is ' + description)

# print(dict(f_tuple)) # can turn a tuple in a dictionary

my_list = ['a', 'b', 'c', 'd']

new_string = ', '.join(my_list)

letters = 'abcdefghijklmnopqrstuvwxyz'

new_string = ', '.join(letters)

# for c in my_list:
#     new_string += c + ', ' # This is expensive as strings are immutable
    
print(new_string)



