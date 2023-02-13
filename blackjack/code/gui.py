from tkinter import Tk, LabelFrame, Label, Entry, Button, Toplevel;
from PIL import ImageTk,Image

class Gui(Tk):

    def __init__(self,title="tk"):
        super().__init__();
        self.minsize(1000,600);
        self.config(bg="green")
        self.title(title)
        self.hit = False;
        self.dd = False;
        self.split = False;
        self.stay = False;
        self.restart = False;
        self.next = False;
        self.destruct = False;

    # setting up the entry field for inputting bet amount
    def set_bet_frame(self):
        self.bet_frame = LabelFrame(self, highlightthickness=0, bd=0,bg="green");
        self.bet_frame.pack()

        self.bet_input = Entry(self.bet_frame)
        self.bet_input.insert(-1, "Enter bet: ")
        self.bet_input.grid(row=0, column=0)

        bet_btn = Button(self.bet_frame, text="Enter Bet", bd=0, command=self.on_enter);
        bet_btn.grid(row=0, column=1, padx=10)

        # starting balance of 3000
        self.balance = Label(self.bet_frame,text="Balance: ",font=("Helvetica",18),bg="green");
        self.balance.grid(row=0,column=2)

    # sets up the frame for the computer hand
    def set_dealer_frame(self):
        self.dealer_frame = LabelFrame(self, bg="green", text="Computer Hand");
        self.dealer_frame.pack(pady=(10, 0))

    # sets up frames for both possible hands of a player
    def set_player_frames(self):
        self.player_frame_one = LabelFrame(self, text="Hand 1", bg="green");
        self.player_frame_one.pack()

        self.player_frame_two = LabelFrame(self,text="Hand 2", bg="green")
        self.player_frame_two.pack();


    # after bet is entered
    def on_enter(self):
        self.bet_input.config(state="disabled")
    # tu update balance initally and when double or split
    def update_balance(self,balance):
        self.balance.config(text="Balance: " + str(balance))

    # set up the dealer hand, hidden one card initially
    def set_dealer_hand(self,card_list=["back"]):
        dealer_card1, dealer_card2, dealer_card3, dealer_card4, dealer_card5 = Label(), Label(), Label(), Label(), Label();
        dealer_card_labels = [dealer_card1, dealer_card2, dealer_card3, dealer_card4, dealer_card5]

        for index, card in enumerate(card_list):
            # GETTING THE IMAGE
            card_image = Image.open(f"../images/{card}.png")
            card_image = card_image.resize((120, 200), Image.Resampling.LANCZOS)
            card_image = ImageTk.PhotoImage(master=self.dealer_frame,image=card_image)

            dealer_card_labels[index] = Label(self.dealer_frame, image=card_image);
            dealer_card_labels[index].grid(row=0, column=index, padx=10);
            dealer_card_labels[index].image = card_image;

    #used to set up hand one no matter split
    def set_player_hand_one(self,card_list=["back","2_of_clubs"]):
        player_card1, player_card2, player_card3, player_card4, player_card5 = Label(), Label(), Label(), Label(), Label();
        player_card_labels = [player_card1, player_card2, player_card3, player_card4, player_card5]

        for index, card in enumerate(card_list):
            # GETTING THE IMAGE
            card_image = Image.open(f"../images/{card}.png")
            card_image = card_image.resize((120, 200), Image.Resampling.LANCZOS)
            card_image = ImageTk.PhotoImage(master=self.player_frame_one,image=card_image)

            player_card_labels[index] = Label(self.player_frame_one, image=card_image);
            player_card_labels[index].grid(row=0, column=index, padx=10);
            player_card_labels[index].image = card_image;

    # runs when split is chosen
    def set_player_hand_two(self,card_list=["ace_of_clubs"]):
        # # for the second hand
        second_player_card1, second_player_card2, second_player_card3, second_player_card4, second_player_card5=Label(),Label(),Label(),Label(),Label();
        second_player_card_labels = [second_player_card1,second_player_card2,second_player_card3,second_player_card4,second_player_card5];

        for index, card in enumerate(card_list):
            # GETTING THE IMAGE
            card_image = Image.open(f"../images/{card}.png")
            card_image = card_image.resize((120, 200), Image.Resampling.LANCZOS)
            card_image = ImageTk.PhotoImage(master=self.player_frame_two,image=card_image)

            second_player_card_labels[index] = Label(self.player_frame_two, image=card_image);
            second_player_card_labels[index].grid(row=0, column=index, padx=10);
            second_player_card_labels[index].image = card_image;

    # displays all the things that player can do(hit,dd,split,stay,results)
    def set_choice_frame(self,hand=0):
        # initialize all the choices to false
        self.hit = False;
        self.dd = False;
        self.stay = False;
        self.next = False;

        self.choice_frame = LabelFrame(self,bg="green");
        self.choice_frame.config(text=f"Hand {hand+1}")
        self.choice_frame.pack(pady=10);

        # hit button
        self.hit_btn = Button(self.choice_frame, text="Hit", command=self.hit_click);
        self.hit_btn.grid(row=0,column=0);

        # double down button
        self.dd_btn = Button(self.choice_frame, text="Double Down", command=self.dd_click);
        self.dd_btn.grid(row=0,column=1);

        # split button
        self.split_btn = Button(self.choice_frame, text="Split", state="disabled", command=self.split_click);
        self.split_btn.grid(row=0,column=2);

        # stay button
        self.stay_btn = Button(self.choice_frame,text="Stay", command=self.stay_click)
        self.stay_btn.grid(row=0,column=3)

        # to view results
        self.next_btn = Button(self.choice_frame, text="Results", command=self.next_click, state="disabled");
        self.next_btn.grid(row=0,column=4)

    # check if the hit button is clicked
    def hit_click(self):
        self.hit = True;

    # check if split is clicked
    def split_click(self):
        self.split = True;

    # check if doubled down
    def dd_click(self):
        self.dd = True;

    # if player stays on hand
    def stay_click(self):
        self.stay = True;

    # check if results buttons is clicked
    def next_click(self):
        self.next = True;

    # check to see if play again is clicked
    def restart_click(self):
        self.restart =  True;

    # when exit window is clicked
    def destruct_click(self):
        self.destruct = True;

    # display who the winner is
    def display_winner(self,lst):
        for index,result in enumerate(lst):
            if result == "Win":
                win = Label(self.top,text=f"Player wins on Hand {str(index+1)}",font=("Arial",36),bg="green");
                win.pack(pady=10);
            elif result == "Loss":
                loss = Label(self.top, text=f"Dealer wins on Hand {str(index + 1)}", font=("Arial", 36), bg="green");
                loss.pack(pady=10);
            else:
                tie = Label(self.top, text=f"It's a push on Hand {str(index + 1)}", font=("Arial", 36), bg="green");
                tie.pack(pady=10)

    # show after the game has ended
    def set_result_frame(self):
        end_frame = LabelFrame(self.top);
        end_frame.pack(pady=10);
        play_again_btn = Button(end_frame,text="Play Again",bg="green",command=self.restart_click);
        play_again_btn.grid(row=0,column=0);
        quit_btn = Button(end_frame,text="Exit", command=lambda :{self.destroy(),self.top.destroy(),self.destruct_click()});
        quit_btn.grid(row=0,column=1);

    # creates another window to display results
    def create_result_screen(self):
        self.top = Toplevel();
        self.top.minsize(500,500)
        self.top.config(bg="green")

    # display how much player won(net)
    def display_winnings(self,gain):
        lb = Label(self.top,text=f"Net Gain: ${str(gain)}");
        lb.pack();

    # restart game when play again
    def restart_game(self):
        self.top.destroy();
        for widget in self.winfo_children():
            widget.destroy();
        self.hit = False;
        self.dd = False;
        self.split = False;
        self.stay = False;
        self.restart = False;
        self.next = False;

