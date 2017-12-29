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
        conductor.hand.add(target.choose_card())


def kill(target):
    """
    The basic action for killing a player's card.
    """
    target.revealed.add(target.choose_card())


def challenge(conductor, target, card):
    """
    The basic action for challenging another
    player's card.
    """
    if card in target.hand:
        kill(conductor)
    else:
        kill(target)


#~~~Card Actions~~~

#General
def coup(conductor, target):
    """
    Pay seven coins and launch a coup against an opponent, 
    forcing that player to lose an influence.
    """
    pay(conductor, self.treasury, 7)
    kill(target)


def income(conductor):
    """
    Take one coin from the treasury.
    """
    pay(self.treasury, conductor, 1)


#Classic