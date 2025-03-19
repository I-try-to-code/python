logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
card= {"Ace":0,"2":1,"3":2,"4":3,"5":4,"6":5 ,"7":6,"8":7,"9": 8,"10": 9,"Jack":10,"Queen":11,"king":12}
deck=[11,2,3,4,5,6,7,8,9,10,10,10,10,]
def blackjack(x):
    if x==1:
        print("\n\nBlackjack\nYou Win")
        refresh()
    else:
        return
    
dealer=[]
my_deck=[]
def refresh():
    x= input("\n\nTo continue the game, press any key to continue: ")
    if(x.isalnum() or x=="" or x==""):
        dealer.clear()   
        my_deck.clear()
        for i in range(2):
            dealer.append(random.choice(list(card.keys())))
            my_deck.append(random.choice(list(card.keys())))
 
def count_dealer(hand):
    return hand[0]

def count(hand):
    
    sum=0
    for i in hand:
        sum+=deck[card[i]]
    if sum>21 and "Ace" in hand:
        sum-=10
    if sum==21:
        blackjack(hand==my_deck)
    return sum


def stand():
    print("dealers deck is ", print_deck(dealer))
    print("dealer Sum: ", count(dealer))
    while count(dealer)<17:
        dealer.append(random.choice(list(card.keys())))
        print("\nDealer draws a card\n")
        print("dealers deck is ", print_deck(dealer))
        print("dealer Sum: ", count(dealer))
        print("\n\n")
        
    deall= count(dealer)
    mecountt= count(my_deck)
     
    if deall>21:
        print(" Dealer Bust\nYou Win")
    elif deall>mecountt:
        print(" You Lose")
    elif deall<mecountt:
        print(" You Win")
    else:
        print(" Draw")
    refresh()

def hit():
    my_deck.append(random.choice(list(card.keys())))
    
    if count(my_deck)>21:
        print("\nYour Cards are:  ", print_deck(my_deck))
        print("Your Sum: ",count(my_deck))
        print("\n\nYou Bust\nYou Lose")
        refresh()

print(logo)
         



for i in range(2):
    dealer.append(random.choice(list(card.keys())))
    my_deck.append(random.choice(list(card.keys())))

def print_deck(deck):
    return ' '.join(deck )

while True:
    print("\n\n\nDealers Cards are:  ",dealer[0] , ", Hidden")
    print("Dealer Sum: ", count_dealer(dealer))
    print("\nYour Cards are:  ", print_deck(my_deck))
    print("Your Sum: ",count(my_deck))
    choice=int(input("\nEnter:\n 1. To Hit\n 2. To Stand: \nYour choice: " ))
    if choice==1:
        hit()
    elif choice==2:
        stand()
    else:
        print("Invalid choice!!!")


