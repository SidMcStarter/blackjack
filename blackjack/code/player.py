from cards import *;
from functions import set_name;


# Main player class
class Player:
    # cards is a list of tuples
    def __init__(self):
        self.split = False;
        # stores the cards for each hand
        self.hands = [[], []]
        # shows the total value of indivdual hand
        self.hands_value = [0,0];
        self.bust = [False, True];
        # container the higher score for eah hand
        self.scores = [0, 0];
        self.balance = 3000
        self.double_down = [False, False]
        self.bets = [0,0];

    # hit a card but also which hand theh player hits
    def hit(self, card, hand):
        self.hands[hand].append(card);

    # displays the hand in the gameboard
    def display_hand(self, hand, game_board):
        player_cards = [*self.hands[hand]]
        for index,cd in enumerate(player_cards):
            player_cards[index] = set_name(cd);
        if hand == 0:
            game_board.set_player_hand_one(player_cards)
        else:
            game_board.set_player_hand_two(player_cards);

    # displays the hand point value on the board
    def display_score(self,hand,game_board):
        score = self.scores[hand];
        text = f"Hand {hand + 1}: {str(score)}"
        if hand == 0:
            game_board.player_frame_one.config(text=text);
        elif hand == 1:
            game_board.player_frame_two.config(text=text);



    # sets the point value of the first hand;
    def set_first_total(self, hand):
        # to get the card face value
        player_cards = [cd[0] for cd in self.hands[hand]]
        # if there is only one ace
        if player_cards.count("A") == 1:
            player_cards.remove("A");
            point = point_value[player_cards[0]];
            self.hands_value[hand] = [1 + point, 11 + point];
            self.scores[hand] = max(1 + point, 11 + point)
        # id there are two ace
        elif player_cards.count("A") == 2:
            self.hands_value[hand] = [2,12];
            self.scores[hand] = 12;
        else:
            point1, point2 = point_value[player_cards[0]], point_value[player_cards[1]];
            self.hands_value[hand] = [point1+point2];
            self.scores[hand] = point1+point2;

    # finds the possible hands values after the first round
    def set_score(self,card,hand):
        point = point_value[card[0]]
        player_scores = [*self.hands_value[hand]];
        # stores all the scores made by the card
        temp_lst = []
        # if there is an ace
        for index, score in enumerate(player_scores):
            # if the new card is an ace
            if "A" in card:
                temp_lst.append(score+1);
                temp_lst.append(score+11);
            else:
                temp_lst.append(score+point);
        self.hands_value[hand] = [*temp_lst]

    # sets the split hand;
    def set_split_hands(self):
        self.hands[1].append(self.hands[0].pop());
        self.hands_value = [[],[]]
        self.split = True;

    # checks the hands value and changes the score;
    def check_bust(self,hand):
        lst = [];
        for val in self.hands_value[hand]:
            if val <= 21:
                lst.append(val);
        if len(lst) == 0:
            self.scores[hand] = 0;
            self.bust[hand] = True;
        else:
            self.scores[hand] = max(lst);
    def restart(self):
        self.split = False;
        # stores the cards for each hand
        self.hands = [[], []]
        # shows the total value of indivdual hand
        self.hands_value = [0, 0];
        self.bust = [False, True];
        # container the higher score for eah hand
        self.scores = [0, 0];
        self.double_down = [False, False]
        self.bets = [0, 0];

