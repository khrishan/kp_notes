__author__ = 'Khrishan'
__title__ = 'Challenge : Program Flow (Part 1)'


# Create a program that takes an IP address entered at the keyboard
# and prints out the number if segments it contains, and the length of each segment.
# 
# An IP address consists of 4 numbers, seperated from each other with a full stop. But
# your program should just count however many are entered
# Examples of the input you may get are:
#
# 127.0.0.1
# .192.168.0.1
# 10.0.123456.255
# 12.16
# 255
#
# So your program should work even with invalid IP Addresses. We're just interested in the
# number of segments and how long each one is.
#
# Once you have a working program, here are some more suggestions for invalid input to test:
#
# .123.45.678.91
# .123.4567.8.9
# .123.156.289.10123456
# 10.10t.10.10
# 12.9.34.6.12.90
# '' - that is, press enter without typing anything
# 
# This challenge is intended to practice for loops and if/else statements, so although
# you could use other techniques ( such as splitting the string up), that's not the  
# approach we're looking for.

ip = input('Please enter an IP address : ')

segment = 1
length = 0

if(len(ip) == 0):
    print('You haven\'t entered anything!')
else:
    for i in range(0, len(ip)):
        if ip[i] == '.':
            print('Segment {} has a length of {}'.format(segment, length))
            segment += 1
            length = 0
        else:
            length += 1
        
        if i == len(ip)-1:
            print('Segment {} has a length of {}'.format(segment, length))
            segment += 1

# The cheeky way of doing this is to put a '.' at the end of the IP address