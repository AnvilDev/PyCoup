"""
This file defines the actions that can be executed
by cards and by players.
"""
#~~~Atomic Actions~~~

def pay(conductor, target, amount):
    """
    The basic action for paying an amount.
    """
    conductor.coins -= amount
    target.coins += amount


def draw(conductor, target):
    """
    The basic action for taking a card.
    """
    if target.is_deck:
        conductor.hand.add(target.hand.pop())
    else:
        conductor.hand.add(target.give_card())


def kill(target):
    """
    The basic action for killing a player's card.
    """
    target.revealed.add(target.reveal_card())


def challenge(conductor, target, card):
    """
    The basic action for challenging another
    player's card.
    """
    if card in target.hand:
        kill(conductor)
    else:
        kill(target)