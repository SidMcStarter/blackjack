from gui import Gui;
from functions import create_a_shoe, first_round, check_winner, get_winnings
from run_split import run_split;
from player import Player;
from computer import Computer;
import time;
if __name__ == "__main__":
    game_board = Gui("Black Jack");

    # setting up the cards, player, and dealer
    shoe = create_a_shoe();
    gamer = Player();
    dealer = Computer();
    while not game_board.destruct:

        # bet input
        game_board.set_bet_frame()
        game_board.update_balance(gamer.balance)

        while game_board.bet_input["state"] == "normal":
            game_board.update()
        bet = game_board.bet_input.get();
        bet = int(bet[bet.index(":")+1:])
        gamer.bet = bet;

        # change balance
        gamer.balance -= gamer.bet;
        gamer.bets[0] = gamer.bet;
        game_board.update_balance(gamer.balance)

        # first round
        first_round(shoe,gamer,dealer);


        # show dealer hand
        game_board.set_dealer_frame();
        dealer.display_hand(0,game_board)

        # show player hand, setting up the score, displaying the score
        game_board.set_player_frames();
        gamer.display_hand(0,game_board)
        game_board.set_choice_frame()
        gamer.set_first_total(0)
        gamer.display_score(0,game_board)

        # check split
        if gamer.hands[0][0][0] == gamer.hands[0][1][0]:
            game_board.split_btn.config(state="normal")
            while not game_board.split and not game_board.hit and not game_board.dd and not game_board.stay:
                game_board.update()

        # if split is active
        if game_board.split:
            # destroy the frame to reload cards
            game_board.player_frame_one.destroy();

            game_board.set_player_frames()
            gamer.set_split_hands();
            game_board.split_btn.config(state="disabled")

            # update bet
            gamer.bets[1] = gamer.bet;
            gamer.balance -= gamer.bet;
            game_board.update_balance(gamer.balance)

            # setting up the automatic hit after splitting
            # hand1 set total and display it
            card = shoe.pop();
            gamer.hit(card,0)
            gamer.display_hand(0,game_board)
            gamer.set_first_total(0)
            gamer.display_score(0,game_board)
            # hand 2 set total and display it
            card = shoe.pop();
            gamer.hit(card,1)
            gamer.display_hand(1,game_board)
            gamer.set_first_total(1)
            gamer.display_score(1,game_board)

        # play on hand 1
        while not gamer.bust[0] and len(gamer.hands[0]) < 5:
            # to see if a button has been clicked
            while not game_board.hit and not game_board.dd and not game_board.stay:
                game_board.update();

            # chooses to hit
            if game_board.hit:
                card = shoe.pop();
                gamer.hit(card,0);
                gamer.display_hand(0,game_board)
                game_board.dd_btn.config(state="disabled")
                gamer.set_score(card,0)
                gamer.check_bust(0);
                gamer.display_score(0,game_board)
                game_board.hit = False;

            # chooses to double down
            elif game_board.dd:
                card = shoe.pop();
                gamer.hit(card,0);
                gamer.display_hand(0,game_board)
                game_board.dd_btn.config(state="disabled")
                game_board.hit_btn.config(state="disabled")
                gamer.set_score(card,0)
                gamer.check_bust(0);
                gamer.display_score(0,game_board)
                # changing balance if double down
                gamer.bets[0] += gamer.bet;
                gamer.balance -= gamer.bet;
                game_board.update_balance(gamer.balance)
                game_board.stay_btn.config(state="disabled")
                break;

            elif game_board.stay:
                game_board.hit_btn.config(state="disabled")
                game_board.dd_btn.config(state="disabled")
                break;

        # play on hand 2
        if game_board.split:
            gamer.bust[1] = False;
            game_board.choice_frame.destroy();
            game_board.set_choice_frame(1);
            while not gamer.bust[1] and len(gamer.hands[1]) < 5:
                # to see if a button has been clicked
                while not game_board.hit and not game_board.dd and not game_board.stay:
                    game_board.update();

                # chooses to hit
                if game_board.hit:
                    card = shoe.pop();
                    gamer.hit(card, 1);
                    gamer.display_hand(1, game_board)
                    game_board.dd_btn.config(state="disabled")
                    gamer.set_score(card, 1)
                    gamer.check_bust(1);
                    gamer.display_score(1, game_board)
                    game_board.hit = False;

                # chooses to double down
                elif game_board.dd:
                    card = shoe.pop();
                    gamer.hit(card, 1);
                    gamer.display_hand(1, game_board)
                    game_board.dd_btn.config(state="disabled")
                    game_board.hit_btn.config(state="disabled")
                    gamer.set_score(card, 1)
                    gamer.check_bust(1);
                    gamer.display_score(1, game_board)
                    # changing balance if double down
                    gamer.bets[1] += gamer.bet;
                    gamer.balance -= gamer.bet;
                    game_board.update_balance(gamer.balance)
                    game_board.stay_btn.config(state="disabled")
                    break;

                elif game_board.stay:
                    game_board.hit_btn.config(state="disabled")
                    game_board.dd_btn.config(state="disabled")
                    break;

        win = "";
        # computer turn to reveal only if the player did not bust on each hand
        if not gamer.bust[0] or not gamer.bust[1]:
            dealer.hidden = False;
            dealer.display_hand(0,game_board)
            # to set the total for the computer hand
            dealer.set_first_total(0);
            dealer.display_score(0,game_board)

            # if the computer hand is less than seventeen, or it busts
            while dealer.scores[0] < 17 and not dealer.bust[0]:
                card = shoe.pop();
                dealer.hit(card,0)
                dealer.set_score(card,0);
                dealer.check_bust(0)
                dealer.display_hand(0,game_board);
                dealer.display_score(0,game_board)

        win = check_winner(gamer,dealer)
        # results code

        game_board.next_btn.config(state="normal");
        while not game_board.next:
            game_board.update();
        game_board.create_result_screen()

        game_board.display_winner(win)
        game_board.set_result_frame()
        game_board.display_winnings(get_winnings(win,gamer));
        game_board.update_balance(gamer.balance)

        while not game_board.restart:
            game_board.update()
        game_board.restart_game()
        gamer.restart();
        dealer.restart()
        dealer.hidden = True;


    game_board.mainloop();

