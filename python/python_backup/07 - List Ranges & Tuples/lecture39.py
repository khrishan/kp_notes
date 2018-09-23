__author__ = 'Khrishan'
__title__ = 'Lists in Python'

# ip = input('Please enter an IP address : ')
# print(ip.count('.'))

parrot_list = ['non pinin', 'no more', 'a stiff', 'bereft of life']

parrot_list.append('A Norwegian Blue')

for state in parrot_list:
    print("This parrot is {}".format(state))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd

#print(numbers.sort()) - doesn't work as its working on the object that already exists - not creating a new one)

# These work however... 
numbers.sort()
print(numbers)

print(sorted(numbers))