""""
This file contains the Card class. The Card class is used to represent a generic Card in the game.

Each card has TWO attributes:

Value: Which specifies its value.
The value for regular color cards ranges from 0 to 9, and D, R and S which stand for Draw Two, Reverse and Skip.

Color: Which specifies the color. Regular cards have colors Red, Green, Blue and Yellow. Special cards have Black
color. Black cards also have different values, viz "Wild" and "Wild Draw Four".

"""

class Card:
    def __init__(self, color, value):
        self.value = value
        self.color = color

    def __repr__(self):
        return "<Card {} {}>".format(self.color, self.value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class UnoCard(Card):

    def __init__(self, color, value):
        self.ALLOWED_COLORS = ["Red", "Blue", "Green", "Yellow", "Black"]
        self.ALLOWED_VALUES = [str(n) for n in range(1,10)] + ["R", "S", "D"]
        self.color = color
        self.value = value


    @property
    def color(self):
        return self._color