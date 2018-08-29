__author__ = 'Khrishan'
__title__ = 'What is Binary'

# for i in range(17):
#     print('{0:>2} in binary is {0:08b}'.format(i))

# for i in range(17):
#     print('{0:>2} in hex is {0:>02x}'.format(i))

# for i in range(17):
#     print('{0:>2} in octal is {0:>02o}'.format(i))

# x = 0x20
# y = 0x0a

# print(x)
# print(y)
# print(x * y)
# print(0b10101010)
# print(0o10)

# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1)
# 
# Write a program that requests a number from the keyboard, then prints out its binary representation.
# 
# Obviously, you could use a format string, but that is not allowed for this
# challenge.
# 
# The program should cater for numbers up to 65535. i.e. (2 ** 16) - 1
# 
# Hint : you will need integer division (//), and modulo (%) to ger the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
# 
# As an optional extra, try to avoid printing leading zeros.
# 
# Once the program is working, modify it to print Octal rather than binary.

value = int(input('Please enter a digit (max 65535) : '))
old_value = int(value)
answer = ''

for i in range(15, -1, -1):
    v = 2 ** i
    if value // v > 0:
        answer += str((value // v))
        value = value % v
    elif answer != '':
        answer += '0'

print('{} in binary is {}'.format(old_value, answer))
