__author__ = 'Khrishan'
__title__  = 'More on Dictionaries'

fruit = {'orange': 'a sweet orange citrus fruit',
         'apple' : 'good for making cider',
         'lemon' : 'a sour, yellow citrus fruit',
         'grape' : 'a small, sweer fruit growing in bunches',
         'lime'  : 'a sour , green citrus fruit',
         'apple' : 'round and crunchy',
        }

print(fruit)

veg = {'cabbage': 'every child\'s favourite',
       'sprouts': 'mmmmm, lovely',
       'spinach': 'can I have some more fruit'
      }

print(veg)

veg.update(fruit) # Update doesn't create a new dictionry (so printing this will return None)

print(veg)

nice_and_nasty = fruit.copy() # when you want to create a new dictionary
nice_and_nasty.update(veg)
print(nice_and_nasty)