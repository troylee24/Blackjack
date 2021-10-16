from card import Card

class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.score = 0
        self.ace_score = 0
    
    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.update_scores(card)

    def update_scores(self, card: Card) -> None:
        self.score += card.value
        if self.ace_score != 0:
            self.ace_score += card.value
        elif card.is_ace:
            self.ace_score = self.score + 10
    
    def is_21(self) -> bool:
        return self.score == 21 or self.ace_score == 21

    def is_bust(self) -> bool:
        return self.score > 21

    def max_score(self) -> int:
        return max(self.score, self.ace_score) if self.ace_score <= 21 else self.score

    def str_scores(self) -> str:
        if self.ace_score != 0 and self.ace_score <= 21:
            return "{} or {}".format(self.score, self.ace_score)
        return str(self.score)            

    def __str__(self) -> str:
        return " ".join(str(card) for card in self.cards)

class DealerHand(Hand):
    def __init__(self) -> None:
        super().__init__()
        self.face_down = True

    def str_scores(self) -> str:
        if not self.face_down:
            return super().str_scores()
        return str(self.cards[0].value)
    
    def __str__(self) -> str:
        if not self.face_down:
            return super().__str__()
        return str(self.cards[0])