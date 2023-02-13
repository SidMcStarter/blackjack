from cards import *
from random import *


# creates a deck in tuple variation: (Card # Card Suit)
def create_a_deck():
    deck = [];
    for suit in suits:
        for card in point_value:
            deck.append((card, suit));
    return deck;


# Creates multiple decks at once
def create_a_shoe(x=6):
    shoe = [];
    for i in range(0, x):
        shoe += create_a_deck();
    shuffle(shoe);
    return shoe;

# creates the hand for the dealer and the player in the first round only
def first_round(shoe, player, comp):
    card1, card2, card3, card4 = shoe.pop(), shoe.pop(), shoe.pop(), shoe.pop();

    card1 = ("A","C")
    card3 = ("A","C");

    player.hit(card1,0);
    player.hit(card3,0);

    comp.hit(card2,0);
    comp.hit(card4,0)

def set_name(card):
    card_name = card[0]
    if "A" in card:
        card_name = "ace";
    elif "J" in card:
        card_name = "jack"
    elif "K" in card:
        card_name = "king";
    elif "Q" in card:
        card_name = "queen";
    return f"{card_name}_of_{suits[card[1]]}"


# check winner for each hand of the player; result is in terms of player
def check_winner(player,comp):
    comp_score = comp.scores[0];
    results = []
    # check hand 1:
    score1 = player.scores[0];
    if score1 < comp_score or player.bust[0]:
        results.append("Loss")
    elif score1 > comp_score:
        results.append("Win")
    else:
        results.append("Push")

    # check hand 2:
    if player.split:
        score2 = player.scores[1];
        if score2 < comp_score or player.bust[1]:
            results.append("Loss")
        elif score2 > comp_score:
            results.append("Win")
        else:
            results.append("Push")
    return results;

# gives total earnings based on win/loss
def get_winnings(results, player):
    old_balance = player.balance + sum(player.bets)
    for index,result in enumerate(results):
        winning = 0;
        if result == "Win":
            winning += player.bets[index] * 2;
            player.balance += winning;
        elif result == "Loss":
            winning -= player.bets[index];
        else:
            player.balance += player.bets[index]
    return player.balance - old_balance