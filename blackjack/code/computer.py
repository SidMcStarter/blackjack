from player import *;
from cards import *;
from functions import set_name;


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.hidden = True;

    # display computer hand: hidden at first
    def display_hand(self, hand, game_board):
        cards = [*self.hands[hand]];
        for index,cd in enumerate(cards):
            if self.hidden and index == 0:
                cards[index] = "back"
            else:
                cards[index] = set_name(cd);
        game_board.set_dealer_hand(cards)

    # display dealer scores on dealer frame
    def display_score(self,hand,game_board):
        score = self.scores[hand];
        if score == 0:
            score = "Bust"
        text = f"Computer Hand: {str(score)}"
        game_board.dealer_frame.config(text=text)
