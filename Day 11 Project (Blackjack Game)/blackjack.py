############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run


import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def user_wins(user_cards, dealer_cards, user_total, dealer_total):
    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total}")
    print("You Win!")
    user_win = True
    
def dealer_wins(user_cards, dealer_cards, user_total, dealer_total):
    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total}")
    print("Dealer Wins! You Lose.")
    dealer_win = True

def draw_game(user_cards, dealer_cards, user_total, dealer_total):
    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_total}")
    print("It's a draw")
    draw_game = True
    

def play_again(finished):
    a = input("Do you want to play again? Type 'y' or 'n' ").lower()
    if a == 'y':
        blackjack()
    elif a == 'n':
        print("Thank you for playing! <3")
        finished = True
         
def blackjack():
    print(logo)
    user_cards = []
    dealer_cards = []
    user_win = False
    dealer_win = False
    draw_game = False
    finished = False
        
    while user_win != True and dealer_win != True and draw_game != True and finished != True:
        
        for i in range(2):
            random_card = random.choice(cards)
            user_cards.append(random_card)
            random_card = random.choice(cards)
            dealer_cards.append(random_card)
        
        print(f"Your initial hand: {user_cards}")
        print(f"Dealer's initial hand: {dealer_cards[0]}")
        
        user_total = user_cards[0] + user_cards[1]
        dealer_total = dealer_cards[0] + dealer_cards[1]
        
        if user_total == 21:
            print("You hit BlackJack!")
            user_wins(user_cards, dealer_cards, user_total, dealer_total)
            play_again(finished)
        elif dealer_total == 21:
            print("Dealer Hits Blackjack!")
            dealer_wins(user_cards, dealer_cards, user_total, dealer_total) 
            play_again(finished)
        else:
            a = False
            while a != True:
                deal_another = input("Do you want to deal another card? y/n ").lower()
                if deal_another == 'y':
                    random_card = random.choice(cards)
                    user_cards.append(random_card)
                    user_total += random_card
                    if 11 in user_cards and user_total > 21:
                        user_total - 10
                    print(f"Your hand: {user_cards}")
                    if user_total > 21:
                        print("You went over 21")
                        dealer_wins(user_cards, dealer_cards, user_total, dealer_total)
                        a = True
                        finished = True
                        play_again(finished)
                    elif user_total == 21:
                        print("You Hit BlackJack!")
                        user_wins(user_cards, dealer_cards, user_total, dealer_total)  
                        a = True
                        play_again(finished)
                elif deal_another == 'n':
                    b = False
                    while b != True:                    
                        if dealer_total <= 17:
                            while dealer_total <= 17:
                                random_card = random.choice(cards)
                                dealer_cards.append(random_card)
                                print(dealer_cards)
                                dealer_total += random_card
                            if 11 in dealer_cards and dealer_total > 21:
                                dealer_total -= 10
                        elif dealer_total == 21:
                                print("Dealer Hits Blackjack!")
                                dealer_wins(user_cards, dealer_cards, user_total, dealer_total)
                                a = True
                                b = True
                                dealer_win = True
                                finished = True
                                play_again(finished)
                        elif dealer_total > 21:
                                print("Dealer went over 21")
                                user_wins(user_cards, dealer_cards, user_total, dealer_total)
                                b = True
                                a = True
                                finished = True
                                play_again(finished)
                        elif user_total == dealer_total:
                                draw_game(user_cards, dealer_cards, user_total, dealer_total)
                                b = True
                                a = True
                                finished = True
                                play_again(finished)
                        elif dealer_total > user_total:
                                dealer_wins(user_cards, dealer_cards, user_total, dealer_total)
                                b = True
                                a = True
                                finished = True
                                play_again(finished)
                        elif user_total > dealer_total:
                                user_wins(user_cards, dealer_cards, user_total, dealer_total)
                                b = True
                                a = True
                                finished = True
                                play_again(finished)
                            




blackjack()







# DRAW
# 1/11 Ace value
