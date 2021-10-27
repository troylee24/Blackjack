from typing import List
from player import BetTooLargeError, Player
from deck import Deck
from hand import DealerHand, Hand
from card import Card
from time import sleep

class Game:
    def __init__(self) -> None:
        self.max_players = 4
        self.deck = Deck()
        self.players: List[Player] = []
        self.dealer_hand: Hand = None
        self.bet_multiple = 5
        self.delay = 0.25

    # CARD HANDLING FUNCTIONS
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

    def gather_bets(self) -> None:
        print()
        sleep(self.delay)
        print("* Bets must be in multiples of ${} *\n".format(self.bet_multiple))
        sleep(self.delay)
        for player in self.players:
            print("Player {}'s chip stack: ${}".format(player.id, player.chips))
            sleep(self.delay)

            while True:
                try:
                    bet = int(input("How much would you like to bet?: $"))
                    if bet <= 0 or bet % self.bet_multiple != 0:
                        print("- Please enter bets in multiples of ${} -".format(self.bet_multiple))
                        continue
                    try:
                        player.make_bet(bet)
                        break
                    except BetTooLargeError:
                        print("- Please check if you have enough chips to make this bet -")
                except ValueError:
                    print("- Please enter bets in multiples of ${} -".format(self.bet_multiple))
            print()
            sleep(self.delay)
    
    # PRINT FUNCTIONS
    def print_scoreboard(self) -> None:
        print("Dealer   | {}".format(self.dealer_hand.max_score()), end="")
        if self.dealer_hand.is_bust(): print(" (BUST!)")
        else: print()
        for player in self.players:
            print("Player {} | {}".format(player.id, player.score()), end="")
            if player.has_bust(): print(" (BUST!)")
            else: print()
        print()

    def evaluate_results(self) -> None:
        print("----- RESULTS -----\n")
        self.print_scoreboard()
        sleep(self.delay)
        
        # dealer result
        if self.dealer_hand.is_bust():
            print("Dealer busted.")
        else:
            print("Dealer ended with {}.".format(self.dealer_hand.max_score()))
        
        # player results
        multipliers = {
            "busted": -1,
            "lost": -1,
            "tied": 0,
            "tied Blackjack": 0,
            "won": 1,
            "won Blackjack": 1.5
        }
        payouts = {}
        for player in self.players:
            if player.has_bust():
                result = "busted"
            elif player.has_blackjack():
                if self.dealer_hand.is_blackjack():
                    result = "tied Blackjack"
                else:
                    result = "won Blackjack"
            else:
                if self.dealer_hand.is_bust():
                    result = "won"
                else:
                    if player.score() > self.dealer_hand.max_score():
                        result = "won"
                    elif player.score() < self.dealer_hand.max_score():
                        result = "lost"
                    else:
                        result = "tied"
            print("Player {} {} with {}.".format(player.id, result, player.score()))
            payout = player.payout(multipliers[result])
            payouts[player] = payout
            sleep(self.delay)
        print()

        print("----- CHIP STACKS -----\n")
        for player in self.players:
            print("Player {} | ${}".format(player.id, player.chips), end="")
            payout = payouts[player]
            if payout < 0:
                print(" (-${})".format(abs(payout)))
            else:
                print(" (+${})".format(abs(payout)))
            sleep(self.delay)
        print()
    
    # MAIN FUNCTION
    def run(self) -> None:
        self.player_count_loop()
        
        while True:
            if not self.game_loop():
                return

    def player_count_loop(self):
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
    
    def game_loop(self) -> bool:
        # READY LOOP
        while True:
            ans = input("Ready to Play? (Y/N): ")
            if ans.upper() == "Y": break
            if ans.upper() == "N": return False
            else: print("- Please answer Y/N -")
        print()

        # initialize hands
        for player in self.players:
            player.hand = Hand()
        self.dealer_hand = DealerHand()

        print("...Shuffling Deck...")
        self.deck.shuffle()
        sleep(self.delay)

        print("...Gathering Bets...")
        self.gather_bets()
        sleep(self.delay)

        print("...Dealing Cards...")
        self.deal_cards()
        sleep(self.delay)
        print()

        # stop game short if dealer has Blackjack
        if self.dealer_hand.is_blackjack():
            print("* Dealer has Blackjack. Checking player hands. *")
            self.evaluate_results()
            return
        
        # play Blackjack for each player
        for player in self.players:
            print("----- Player {}'s turn -----\n".format(player.id))
            sleep(self.delay)

            # check if Blackjack
            if player.hand.is_21():
                print("Hand: {} ({})".format(player.hand, player.hand.str_scores()))
                print("\n* Congratulations, you have BLACKJACK!!! *\n")
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
                    sleep(self.delay)
                    print("\n* STAND! *\n")
                    break
                else: print("- Please answer Hit/Stand -")
            sleep(self.delay)

        # play Blackjack for dealer
        print("----- Dealer's turn -----\n")
        self.dealer_hand.face_down = False
        while True:
            print("Dealer: {} ({})".format(self.dealer_hand, self.dealer_hand.str_scores()))
            sleep(self.delay)
            if self.dealer_hand.max_score() > 16:
                break
            self.draw_card(self.dealer_hand)
        
        if self.dealer_hand.is_bust():
            print("\n* DEALER BUSTS *\n")
        else:
            print("\n* DEALER STANDS WITH {} *\n".format(self.dealer_hand.max_score()))
        sleep(self.delay)
        
        # evaluate game outcome
        self.evaluate_results()
        sleep(self.delay)

if __name__ == '__main__':
    game = Game()
    game.run()