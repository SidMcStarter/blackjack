from tkinter import *
from tkmacosx import *;
from PIL import ImageTk, Image
from player import Player;
#
window = Tk();
# window.geometry("1000x600")
window.minsize(1000,600)
# window.maxsize(1000,600)
window.config(bg="green",)

dealer_card1,dealer_card2,dealer_card3,dealer_card4,dealer_card5 = Label(),Label(),Label(),Label(),Label();
dealer_card_labels = [dealer_card1,dealer_card2,dealer_card3,dealer_card4,dealer_card5]

player_card1,player_card2,player_card3,player_card4,player_card5=Label(),Label(),Label(),Label(),Label();
player_card_labels = [player_card1,player_card2,player_card3,player_card4,player_card5]

def setBalance(balance=3000):
    balance_lbl = Label(bet_frame,text=f"Balance: ${balance}",font=("Helvetica",18),bg="green")
    balance_lbl.grid(row=0,column=2,padx=(10,0))

def onEnter():
    global bet_input;
    bet_input.config(state="disabled");
    bet = bet_input.get();
    bet = int(bet[bet.index(":")+1:])
    print(bet);
    setBalance()
    setCompHand()
    setPlayerHand()
    setPlayerHand2()
    deal_btn.configure(state="normal");


def setCompHand(card_list=["back","2_of_clubs","back"]):
    global dealer_card_labels;

    for index,card in enumerate(card_list):
        # GETTING THE IMAGE
        image = Image.open(f"../images/{card}.png")
        image = image.resize((120, 200), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)

        dealer_card_labels[index] = Label(dealer_frame,image=image);
        dealer_card_labels[index].grid(row=0,column=index,padx=10);
        dealer_card_labels[index].image = image;

def setPlayerHand(card_list=["ace_of_clubs"]):
    global player_card_labels;

    for index,card in enumerate(card_list):
        # GETTING THE IMAGE
        image = Image.open(f"../images/{card}.png")
        image = image.resize((120, 200), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)

        player_card_labels[index] = Label(player_frame,image=image);
        player_card_labels[index].grid(row=0,column=index,padx=10);
        player_card_labels[index].image = image;

def setPlayerHand2(card_list=["ace_of_clubs"]):
    global player_card_labels;
    for index,card in enumerate(card_list):
        # GETTING THE IMAGE
        image = Image.open(f"../images/{card}.png")
        image = image.resize((120, 200), Image.Resampling.LANCZOS)
        image = ImageTk.PhotoImage(image)

        player_card_labels[index] = Label(player_frame2,image=image);
        player_card_labels[index].grid(row=1,column=index,padx=10);
        player_card_labels[index].image = image;


# deals with the bet amount
bet_frame = LabelFrame(window,bg="green",highlightthickness=0,bd=0);
bet_frame.pack()

bet_input = Entry(bet_frame,bd=0)
bet_input.insert(-1,"Enter bet: ")
bet_input.grid(row=0,column=0)

bet_btn = Button(bet_frame,text="Enter Bet",bd=0,command=onEnter);
bet_btn.grid(row=0,column=1,padx=(10,0))



# deals with the dealer
dealer_frame = LabelFrame(window,bg="green",text="Computer Hand");
dealer_frame.pack(pady=(10,0))

player_frame = LabelFrame(window,text="Player Hand",bg="green");
player_frame.pack()

player_frame2 = LabelFrame(window,text="Player Hand 2",bg="green")
player_frame2.pack(pady=20)

deal_btn = Button(window,text="Deal", state="disabled");
deal_btn.pack()

# window.mainloop()