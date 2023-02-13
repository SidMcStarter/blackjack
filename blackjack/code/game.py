import time;
from player import *
from functions import *;
from computer import *
from winner import end_game;

print("Starting Balance: 3000")
shoe = create_a_shoe();
player1 = Player();
comp = Computer();
if player1.balance >= 0:
    while player1.balance >= 0:
        print()
        bet = int(input("Enter your Bet: "))
        player1.bets.append(bet)
        if bet > player1.balance:
            continue
        player1.balance -= bet;
        player1.bet = bet;
        print()

        first_round(shoe,player1,comp)


        print("Comp")
        comp.display_comp_hand();
        print()

        print("Player")
        player1.get_first_total()
        player1.display_hand()
        print()


        # split
        if player1.check_split():
            # carry out the split
            splits = str(input("Would you like to split(y/n): ")).lower()
            print()
            if "y" in splits:
                player1.balance-=bet;
                player1.bets.append(bet)

                player1.set_split_hand()
                player1.hit(shoe.pop());
                player1.hit(shoe.pop(),1);

                player1.get_first_total();
                player1.display_hand()
                print()

                player1.get_first_total(1)
                player1.display_hand(1)
                print()

                while(not player1.bust[0]):
                    # double down option on the first hand
                    if len(player1.hands[0]) == 2 and player1.balance >= player1.bet:
                        play = str(input("Hit,Stay,Double Down on Hand 1(h/s/d): ")).lower();
                    else:
                        play = str(input("Hit,Stay on Hand 1(h/s): ")).lower();

                    if "h" in play:
                        card = shoe.pop()
                        print_hand(player1,card,0)
                    elif "d" in play:
                        # check bet
                        player1.double_down[0] = True;
                        card = shoe.pop()
                        print_hand(player1, card,0)
                        player1.balance-=bet;
                        player1.bets[0] += bet;
                        break;
                    else:
                        break;
                    # check to see if the player busted on the first hand
                    if player1.bust[0]:
                        print("Comp Wins on Hand 1")
                        print()
                        player1.bets.pop(0);

                # second hand
                player1.bust[1] = False;
                while(not player1.bust[1]):
                    # double down option on the second hand
                    if len(player1.hands[1]) == 2 and player1.balance >= player1.bet:
                        play = str(input("Hit,Stay,Double Down on Hand 2(h/s/d): ")).lower();
                        print()
                    else:
                        play = str(input("Hit,Stay on Hand 2(h/s): ")).lower();
                        print()
                    if "h" in play:
                        card = shoe.pop()
                        print_hand(player1,card,1)
                    elif "d" in play:
                        card = shoe.pop()
                        print_hand(player1, card,1)
                        player1.balance-=bet;
                        player1.bets[1] += bet;
                        player1.double_down[1] = True;
                        break;
                    else:
                        print()
                        break;

                    if player1.bust[1]:
                        print("Comp Wins on Hand 2")
                        player1.bets.pop(1);
                        print()
        # no split scenario
        if not player1.split:
            while(not player1.bust[0]):
                if len(player1.hands[0]) == 2 and player1.balance >= player1.bet:
                    play = str(input("Hit,Stay,Double Down on Hand(h/s/d): ")).lower();
                else:
                    play = str(input("Hit,Stay on Hand(h/s): ")).lower();
                if "h" in play:
                    card = shoe.pop()
                    print_hand(player1, card,0)
                elif "d" in play:
                    card = shoe.pop()
                    print_hand(player1, card,0)
                    player1.balance-=bet;
                    player1.bets[0] += bet;
                    player1.double_down[0] = True;
                    break;
                else:
                    print()
                    break
                if player1.bust[0]:
                    print("Comp Wins")
                    print()
                    player1.bets.pop(0)
                    time.sleep(1)

        # print(player1.hands)
        # print(player1.hands_value)
        # print(player1.score)
        # print(player1.bust)
        # computer game

        if not player1.bust[0] or not player1.bust[1]:
            comp.hidden = False;
            print("Comp")
            comp.get_first_total()
            comp.display_comp_hand();
            while not comp.bust[0] and (comp.score[0] < 17):
                time.sleep(1.5)
                card = shoe.pop()
                comp.hit(card)
                comp.display_hand()
                comp.get_score(card)
                print()
            time.sleep(1)
        end_game(player1,comp)


















