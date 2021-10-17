from hand import Hand
import itertools

class BetTooLargeError(Exception):
    """Raised when a bet is too large"""
    pass

class Player:
    id_iter = itertools.count()

    def __init__(self, chips=100) -> None:
        self.id = next(Player.id_iter)
        self.chips = chips
        self.hand: Hand = None
        self.bet = 0
    
    def payout(self, multiplier: int) -> int:
        amount = self.bet * multiplier
        self.chips += amount
        self.bet = 0
        return int(amount)

    def make_bet(self, bet: int) -> None:
        if self.chips - bet < 0:
            raise BetTooLargeError
        self.bet = bet

    def score(self) -> int:
        return self.hand.max_score()
    
    def has_bust(self) -> bool:
        return self.hand.is_bust()

    def has_blackjack(self) -> bool:
        return self.hand.is_blackjack()