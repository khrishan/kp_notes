__author__ = 'Khrishan'
__title__  = 'Reading and Writing Text Files'

# cities = ['Adelaide', 'Alice Springs', 'Darwin', 'Melbourne', 'Sydney']

# Text is written to a buffer then the buffer sends the text to the text file
# Closing file will cause the buffer to be flushed
# 

# with open('cities.txt', 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file flush=True) # not recommended to use the flush parameter

# cities = []

# with open('cities.txt', 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n')) # each new line has a \n at the end of the file, by using .strip, this will remove it.

# print(cities)
# for city in cities:
#     print(city)

# imelda = 'More Mayhem', 'Imelda May', 2011, (
#     (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
# )

# with open('imelda3.txt', 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open('imelda3.txt', 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents) # not the best way to get contents out of a file as 
print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)

# a = append
# t = text mode
