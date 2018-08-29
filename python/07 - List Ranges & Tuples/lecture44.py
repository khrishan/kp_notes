__author__ = 'Khrishan'
__title__ = 'More About Ranges'

# print(range(0,100)[::-2] == range(99,0,-2))

# for i in range(0, 100, -2):
#     print(i)

# [::] is a slice. default start = 0, default stop is the end of the sequence, default step = 1 [0:length:1]

# backString = 'egaugnal lufrewop yrev a si nohtyP'
# print(backString[::-1])

# Challenge - work out what it is going to do before you running it?
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)
