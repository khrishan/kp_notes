# Give the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separaing them with a comma.)

imelda = 'More Mayhem', 'Emilda May', 2011, (
    (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
)

title, artist, year, tracks = imelda
print('Title  : {}'.format(title))
print('Artist : {}'.format(artist))
print('Year   : {}'.format(year))
print('')
print('Tracks : ')
for track in tracks:
    num, title = track
    print('\t{} - {}'.format(num, title))

# If you have a list in a tuple, then you can modify the list within it