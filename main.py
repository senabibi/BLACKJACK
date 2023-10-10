
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
import os
def deal_card():
   
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0        
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "You Lose"
    elif user_score==0:
        return "You Win"
    elif user_score>21:
        return "You Lose"
    elif computer_score>21:
        return "You Win"  
    elif user_score>computer_score:
        return "You Win"   
    else:
        return "You Lose"       

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_over=False
    for i in range(2):
        new_card=deal_card()
        user_cards.append(new_card)
        computer_cards.append(deal_card())
    while not is_over:
        user_score=calculate_score(user_cards)  
        computer_score=calculate_score(computer_cards) 
        print(f"Your cards: {user_cards},current score: {user_score}")
        print(f" Computer' first card :{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_over=True
        else:
            user_should_deal=input("Do you wanna another card 'y' or pass 'n':")
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"Your final hand:{user_cards},final score: {user_score}")
    print(f" Computer's final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score,computer_score))

while input("Do you wanna start playing Blackjack?(yes for 'y' no for 'n')")=="y":
    os.system('cls')
    play_game()
