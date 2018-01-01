"""
This class handles an instance of a player.
"""
class Player(object):

    def __init__(self, name):
        self.name = name
        self.revealed = []
        self.hand = []

    def reveal_card(self):
        #Do some javascript
        return card