from typing import Dict, List
from player import Player
from deck import Deck
from hand import DealerHand, Hand
from time import sleep

class Game:
    def __init__(self) -> None:
        self.max_players = 4
        self.deck = Deck()
        self.players: List[Player] = []
        self.dealer_hand: Hand = None
        self.scores: Dict[int, int] = {}
        self.delay = 0.5

    def draw_card(self, hand: Hand) -> None:
        card = self.deck.draw()
        hand.add_card(card)

    def deal_cards(self) -> None:
        for _ in range(2):
            # deal to players
            for player in self.players:
                self.draw_card(player.hand)
            # deal to dealer
            self.draw_card(self.dealer_hand)

    def print_scoreboard(self):
        print("SCORES:")
        for id, score in self.scores.items():
            print("Player {} | {}".format(id, score))
        print("Dealer   | {}".format(self.dealer_hand.max_score()))
        print()

    def run(self) -> None:
        # PLAYER COUNT LOOP
        while True:
            try:
                num_players = int(input("Number of Players: "))
            except ValueError:
                print("- Please enter a number - ")
                continue

            if 1 <= num_players <= self.max_players:
                for _ in range(num_players):
                    self.players.append(Player())
                break
            else:
                print("- Please enter a number between 1 and {} -".format(self.max_players))

        # GAME LOOP
        while True:
            # READY LOOP
            while True:
                ans = input("Ready to Play? (Y/N): ")
                if ans.upper() == "Y": break
                if ans.upper() == "N": return
                else: print("- Please answer Y/N -")
            print()

            # initialize hands
            for player in self.players:
                player.hand = Hand()
                self.scores[player.id] = 0
            self.dealer_hand = DealerHand()

            print("...Shuffling Deck...")
            self.deck.shuffle()
            sleep(self.delay)

            print("...Dealing Cards...")
            self.deal_cards()
            sleep(self.delay)
            print()
            
            # play Blackjack for each player
            for player in self.players:
                print("----- Player {}'s turn -----\n".format(player.id))
                sleep(self.delay)

                # check if Blackjack
                if player.hand.is_21():
                    print("Hand: {} ({})".format(player.hand, player.hand.str_scores()))
                    print("\n* Congratulations, you have BLACKJACK!!! *\n")
                    self.print_scoreboard()
                    sleep(self.delay)
                    continue

                print("Dealer's Hand: {} ({})\n".format(self.dealer_hand, self.dealer_hand.str_scores()))
                sleep(self.delay)

                # HIT/STAND LOOP
                while True:
                    print("Hand: {} ({})".format(player.hand, player.hand.str_scores()))
                    sleep(0.25)
                    ans = input("Hit or Stand?: ")
                    if ans.capitalize() == "Hit":
                        self.draw_card(player.hand)
                        if player.hand.is_21(): 
                            print("Hand: {} ({})".format(player.hand, player.hand.str_scores()))
                            sleep(self.delay)
                            print("\n* NICE, 21! *\n")
                            break
                        if player.hand.is_bust():
                            print("Hand: {} ({})".format(player.hand, player.hand.str_scores()))
                            sleep(self.delay)
                            print("\n* BUST! *\n")
                            break
                    elif ans.capitalize() == "Stand":
                        self.scores[player.id] = player.hand.max_score()
                        sleep(self.delay)
                        print("\n* STAND! *\n")
                        break
                    else: print("- Please answer Hit/Stand -")
                sleep(self.delay)

                self.print_scoreboard()
                sleep(self.delay)

            # play Blackjack for dealer
            print("----- Dealer's turn -----\n")
            self.dealer_hand.face_down = False
            while True:
                print("Dealer: {} ({})".format(self.dealer_hand, self.dealer_hand.str_scores()))
                if self.dealer_hand.max_score() > 16:
                    break
                self.draw_card(self.dealer_hand)
                sleep(self.delay)
            
            if self.dealer_hand.max_score() > 21:
                print("\n* DEALER BUSTS *\n")
            else:
                print("\n* DEALER STANDS WITH {} *\n".format(self.dealer_hand.max_score()))

            self.print_scoreboard()
            sleep(self.delay)

            # evaluate game outcome

if __name__ == '__main__':
    game = Game()
    game.run()