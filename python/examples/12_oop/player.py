class Player(object):
    
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0
    
    # By putting an underscore before the method name, we are 'hiding' the methods.
    # Well, not really hiding them, just using the convention that is
    # (don't use them unless you know what you are doing)

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):

        if lives >=0:
            self._lives = lives
        else:
            print('Lives can not be negative!')
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print('Level can not be less than one')
    
    lives = property(_get_lives, _set_lives) # This is how you would define the property, without the decerator.
    level = property(_get_level, _set_level)

    @property # This takes care of the getter required... through the use of a decerator
    def score(self):
        return self._score

    @score.setter # This takes care of the setter required... through the use of a decerator
    def score(self, score):
        self._score = score

    # When you print an object, Python will look for an __str__ method (which is below).
    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}'.format(self)

"""
Challenge 

Modify the Player class so that the player's scores are increased by one thousand every time their level increases by one.

So if they jump up two levels, they'll get a bonus of two thousand added to their score.

If the player drops back a level, they'll lose one thousand for each level they drop back

They can't do below Level One, so your solution should prevent that from happening.

The aim of this cahllenge is to practice properties,
so although it may make more sense to add methods to increase and decrease the level,
please don't do it that way, use a property.
"""
