__author__ = 'Khrishan'
__title__ = 'More Advance If, ElIf and Else Programming'

#age = int(input('How old are you? : '))

# if age >= 16 and age <=65:
#     print('Have a good day at work!')

# if 16 <= age <= 65:
#     print('Have a good day at work!')

# if (age < 16) or (age > 65):
#     print("Enjoy your free time!")
# else:
#     print("Have a good day at work!")

# In Python, true = 1, false = 0 - so non zero values will evaluate to false
# There is a bool() funtion

# print("""False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5} 
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# x = input('Please enter some text : ')
# if x:
#     print('You entered \'{}\''.format(x))
# else:
#     print('You did not enter any text!')

print(not False) # prints True
print(not True)  # prints False

# IN keyword

parrot = 'Norwegian Blue'

letter = input('Enter a character: ')

if letter in parrot:
    print('Give me an {}, Bob'.format(letter))
else:
    print('I do not need that letter')

# B is different to b