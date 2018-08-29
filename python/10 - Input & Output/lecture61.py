__author__ = 'Khrishan'
__title__  = 'Reading and Writing Text Files'

# jabber = open('sample.txt', 'r')

# r = read
# w = write

# for line in jabber:
#     if 'jabberwock' in line.lower():
#         print(line, end='')

# with open('sample.txt', 'r') as jabber:
#     for line in jabber:
#         if 'jabberwock' in line.lower():
#             print(line, end='')

with open('sample.txt', 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

with open('sample.txt', 'r') as jabber:
    lines = jabber.readlines()
    print(lines)