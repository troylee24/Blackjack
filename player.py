from hand import Hand
import itertools

class Player:
    id_iter = itertools.count()

    def __init__(self, chips=100) -> None:
        self.id = next(Player.id_iter)
        self.chips = chips
        self.hand: Hand = None