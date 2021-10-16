class Card:
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.value = 0
        self.is_ace = False

        if rank in {'J', 'Q', 'K'}:
            self.value = 10
        elif rank == 'A':
            self.value = 1
            self.is_ace = True
        else:
            self.value = int(rank)
    
    def __radd__(self, other) -> int:
        return int(self.rank) + other

    def __str__(self) -> str:
        return "{}{}".format(self.rank, self.suit)

