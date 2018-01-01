"""
This class deals with an instance of a game.
"""
import cards.*


class Game(object):

    def __init__(self, game_type, players, characters):
        
        self.card_set = [gen1 = Coup(), gen2 = Income()]

        if game_type == "classic":
            self.card_set += [gen3 = Foreign_Aid()]
        elif game_type == "reformation":
            self.card_set += [gen3 = Foreign_Aid(),
                              gen4 = Allegiance()]
        self.card_set += characters
