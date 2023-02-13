from player import *
from functions import *
def end_game(player,comp):
    for index,bust in enumerate(player.bust):
        if not bust:
            win = check_winner(player,comp,index);
            if "dub" in win:
                player.balance += player.bets[index] * 2;
            elif "tie" in win:
                player.balance += player.bets[index];
            else:
                pass;
    print("Balance: " + str(player.balance))
    player.restart();
    comp.restart();
    comp.hidden = True;
