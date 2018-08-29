__author__ = 'Khrishan'

greeting = 'Bruce'
Greeting = 'There'
_myName = 'Tim'
Tim45 = 'Good'
Tim_Was_57 = 'Hello'

print(Tim_Was_57 + ' ' + greeting)

age = 24
print(age)
print(greeting + str(age))

a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a ** b) # To the power of
print(a / b) # Returns value as a float
print(a // b) # Returns value as an integer
print(a % b)

# Why does range 1 -4 print 0,1,2,3??
# Python ranges go up to - but not including the stop value...
# Humans tend to start indexing at 1 - but computers index at 0
for i in range(1 , 4):
    print(i)

# Math Follows BIDMAS!!!   

c = a + b
d = c / 3
e = d - 4
print(e * 12)


# STRINGS

parrot = 'Norwegian Blue'
print(parrot[3]) # Prints w (the character at index 3)
print(parrot[-1]) # counts backwards
print(parrot[0:6]) # prints the first 6 characters - 0 is where to start , 6 = length
print(parrot[:6]) # same as above (default start is 0)
print(parrot[6:]) # starts at 6 and prints the rest
print(parrot[-4:-2])
print(parrot[0:6:3])

number = '9,223,372,036,854,775,807'
print(number[1::4])
numbers= '1, 2, 3, 4, 5, 6, 7, 8, 9'
print(number[1::3])

string1 = 'he\'s '
string2 = 'probably '
print(string1 + string2)

print('Hello ' * 5)

today = 'friday'
print('day' in today)
print('fri' in today)
print('thur' in today)
print()


