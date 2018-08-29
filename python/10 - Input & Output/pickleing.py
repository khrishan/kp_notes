# when an object is pickled, 
import pickle

# What is Pickle in Python?

# It is used for serializing and de-serializing a Python object structure.
# Any object in python can be pickled so that it can be saved on disk.
# What pickle does is that it “serialises” the object first before writing it to file.
# Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
# The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

# imelda = 'More Mayhem', 'Emilda May', 2011, (
#     (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
# )

# with open('imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open('imelda.pickle', 'rb') as pickle_file:
#     imelda2 = pickle.load(pickle_file)

# print(imelda2)

# pickle isn't backwards compatible


imelda = 'More Mayhem', 'Emilda May', 2011, (
    (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')
)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open('imelda.pickle', 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=3)
    pickle.dump(even, pickle_file, protocol=3)
    pickle.dump(odd, pickle_file, protocol=3)
    pickle.dump(2998302, pickle_file, protocol=3)

# can also use pickle.HIGHEST_PROTOCOL , pickle.DEFAULT_PROTOCOL

with open('imelda.pickle', 'rb') as pickle_file:
    imelda2     = pickle.load(pickle_file)
    odd_list    = pickle.load(pickle_file)
    x           = pickle.load(pickle_file)
    even_list   = pickle.load(pickle_file)
    

print(imelda2)

print('-' * 40)

print(odd_list)

print('-' * 40)

print(even_list)

print('-' * 40)

print(x)

