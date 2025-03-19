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
def blackjack():
    print("Blackjack\nYou Win")
    

dealer=[]
my_deck=[]
def count(hand):
    sum=0
    for i in hand:
        cardd=deck[card[i]]
        if cardd=='11':
            if sum+11<=21:
                sum+=11
            else:
                sum+=1
        else:
            sum+=cardd
    if sum==21:
        blackjack()
    return sum


def stand():
    while count(dealer)<17:
        dealer.append(random.choice(card))
    deall= count(dealer)
    mecountt= count(my_deck)
    if deall>21:
        print("Dealer Bust\nYou Win")
    elif deall>mecountt:
        print("You Lose")
    elif deall<mecountt:
        print("You Win")
    else:
        print("Draw")

def hit():
    my_deck.append(random.choice(card))
    if count(my_deck)>21:
        print("You Bust\nYou Lose")

print(logo)
         
for i in range(2):
    dealer.append(random.choice(list(card.keys())))
    my_deck.append(random.choice(list(card.keys())))

while True:
    print("Dealers Cards are:  ",dealer[0] , ", Hidden")
    print("Dealer Sum: ", count(dealer))
    print("\nYour Cards are:  ",my_deck)
    print("Your Sum: ",count(my_deck))
    choice=int(input("\nEnter:\n 1. To Hit\n 2. To Stand: \nYour choice: " ))
    if choice==1:
        hit()
    elif choice==2:
        stand()
    else:
        print("Please enter a Valid Choice :")


