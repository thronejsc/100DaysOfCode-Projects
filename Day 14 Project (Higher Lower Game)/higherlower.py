from random import randint
from art import logo, vs
from game_data import data
from os import system   


clear = lambda: system('cls')

def compare(a, b, score, game_over, choose):
    if choose == 'a':
            if a['follower_count'] > b['follower_count']:
                clear()
                score += 1
                a = b            
            else:
                clear()
                print(logo)
                print(f"Sorry that's wrong. Final score: {score}")
                game_over = True
    elif choose == 'b':
            if b['follower_count'] > a['follower_count']:
                score += 1
                a = b
                clear()
            else:
                clear()
                print(logo)
                print(f"Sorry that's wrong. Final score: {score}")
                game_over = True
    
    return a, b, score, game_over, choose
    
def play_again():
    again = input("Do you want to play again? y/n ").lower()
    if again == 'y':
        clear()
        higher_lower()
    elif again == 'n':
        print("Thank you for playing! <3")
        clear()
    
def higher_lower():
    game_over = False
    score = 0
    random_number = randint(0, len(data) - 1)
    a = data[random_number]
    while game_over != True:
        print(logo)
        if score > 0:
            print(f"You're right! Current score {score}")
        
        print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")

        print(vs)
        random_number = randint(0, len(data))
        b = data[random_number]
        print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.") 

        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        a, b, score, game_over, choose = compare(a, b, score, game_over, choose)

    play_again()
                
        
        
higher_lower()