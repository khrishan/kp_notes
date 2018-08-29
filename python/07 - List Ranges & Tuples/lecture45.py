__author__ = 'Khrishan'
__title__ = 'Ordered Sets with Tuples'

# Tuples are an 'ordered set of data', which are 'immutable'  -  you cannot modify them

t = 'a', 'b', 'c'

print(t)

print('a', 'b', 'c')
print(('a', 'b', 'c'))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = 'Nightflight', 'Budgie', 1981
imelda = 'More Mayhem', 'Emilda May', 2011, (
    (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
)
metallica = 'Ride the Lightning', 'Metallica', 1984

# print(metallica)
# print(metallica[0]) 

# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

# metallica2 = ['Ride the Lightning', 'Metallica', 1984]
# print(metallica2)
# metallica2[0] = 'Master of Puppets'
# print(metallica2)

# title, artist, year = imelda  # unpacking the tuple
# print(title)
# print(artist)
# print(year)

# As the right hand side is evaluated before the left hand side - this is how things get evaluated

# a, b = 12, 13
# a, b = b, a     # a = 13, b = 12

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)