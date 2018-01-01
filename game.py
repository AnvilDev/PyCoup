"""
This class deals with an instance of a game.
"""
import cards.*


class Game(object):

    def __init__(self, game_type, players):
        if game_type == "classic":
            self.current_cards = [duke, ambassador, captain,
                                  assassin, contessa]
        elif game_type == "reformation":
            self.current_cards = [allegiance,
                                  inquisitor, duke, ambassador, captain,
                                  assassin, contessa]
        elif game_type == "rebellion":
            self.current_cards = []
