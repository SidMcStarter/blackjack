def run_split(game_board,player):
    player.set_split_hands();
    print(player.hands)
    game_board.display_hand();
    # initial hand setup