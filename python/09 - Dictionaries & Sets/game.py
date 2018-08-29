# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do present) No change should
# be needed to the actual code.
# 
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determing which way to go.
locations = {0: 'You are sitting in front of a computer learning Python',
             1: 'You are standing at the end of a road before a small brick building',
             2: 'You are at the top of a hill',
             3: 'You are inside a building, a well house for a small stream',
             4: 'You are in a valley beside a stream',
             5: 'You are in a forest'
            }

exits = {0: {'Q': 0},
         1: {'N': 5, 'E': 3, 'S': 4, 'W': 2, 'Q': 0},
         2: {'N': 5, 'Q': 0},
         3: {'W': 1, 'Q': 0},
         4: {'N': 1, 'W': 2, 'Q': 0},
         5: {'W': 2, 'S': 1, 'Q': 0},
        }

namedExits = {1:{'2': 2, '3': 3, '5': 5, '4': 4},
              2:{'5': 5},
              3:{'1': 1, '2': 2},
              4:{'1': 1, '2': 2},
              5:{'2': 2, '1': 1}
             }

user_inputs = { 'quit'     : 'Q',
                'exit'     : 'Q',
                'go north' : 'N',
                'go south' : 'S',
                'go east'  : 'E',                
                'go west'  : 'W',
                'north'    : 'N',
                'south'    : 'S',
                'east'     : 'E',
                'west'     : 'W',
                'road'     : '1',
                'hill'     : '2',
                'building' : '3',
                'valley'   : '4',
                'forest'   : '5'
              }

loc = 1
while True:
    available_exits = ', '.join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        all_exits = exits[loc].copy()
        all_exits.update(namedExits[loc])
    
    direction = input('Available exits are {} : '.format(available_exits.upper())).upper()
    print()

    if direction.lower() in user_inputs:
        direction = user_inputs[direction.lower()]

    print(direction)
    print(all_exits)

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print('You cannot go in that direction')